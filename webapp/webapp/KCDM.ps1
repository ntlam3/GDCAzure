    
Disconnect-AzAccount
$Error.Clear()
Add-Type -AssemblyName PresentationFramework
do{
    Write-Output "Connect to Next_CDM"
    #$slide7="C:\Log\"+$sub+"-slide2.txt"
    #$list='EUR-PRD-rg','EUR-DEV-rg'
    #$listtemp=Get-AzResourceGroup
    #$list=$listtemp.ResourceGroupName
    #Write-Output $list
    #$files=@($slide6,$slide7)
    #foreach ($file in $files)
    #{
    Connect-AzAccount -ErrorAction SilentlyContinue
    #Connect-AzureAD -TenantId "2ed43249-694c-4259-aa5e-b86af0e8d87c" -ErrorAction SilentlyContinue
    $sub=Get-AzSubscription -TenantId "2ed43249-694c-4259-aa5e-b86af0e8d87c" -ErrorAction SilentlyContinue
    Write-Output "Subscription details:"
    Write-Output $sub.Name
}
while ($sub.Name -ne "Next_CDM")
Select-AzSubscription -SubscriptionName $sub.Name -ErrorAction SilentlyContinue
$rg=@('KR-PROD-rg','KR-DEV-rg','KR-QA-rg')
$slide="./templates/"+$sub.Name+"-slide.txt"
    If ((-not(Test-Path -Path $slide)))
    {
        New-Item -Path $slide
    }
    else{
        Clear-Content -Path $slide
    }
    #}
foreach ($item in $rg)
    {
        Write-Output $item
        $vm=Get-AzVM |Where-Object ResourceGroupName -eq $item
        $disklist=Get-AzDisk -ResourceGroupName $item
        $lblist=Get-AzLoadBalancer -ResourceGroupName $item
        $stracc=Get-AzStorageAccount -ResourceGroupName $item
        $nwinterface=Get-AzNetworkInterface -ResourceGroup $item
        $pubiplist=Get-AzPublicIpAddress -ResourceGroupName $item
        $apgwlist=Get-AzApplicationGateway -ResourceGroup $item
        $appser=Get-AzWebApp -ResourceGroup $item
        
        #Write-Output "--------Slide 7--------" >> $file
        Write-Output "Total VM in $item" $vm.Name.Count >> $slide6
        #$vm.Name.Count >> $file
        Write-Output "Total Disk in $item" $disklist.Name.Count >> $slide
        $GB=0
        $unused_disk=0
        foreach ($diskitem in $disklist)
        {
            #Write-Output $diskitem.ManagedBy >> $file
            $GB=$GB+$diskitem.DiskSizeGB
            if ($null -eq $diskitem.ManagedBy)
            {
                $unused_disk=$unused_disk+1
            }
        }
        Write-Output "Total GB of disks in $item" $GB >> $slide
        Write-Output "Total LB in $item" $lblist.Name.Count >> $slide
        Write-Output "Total App Gateway in $item" $apgwlist.Name.Count >> $slide
        $B=0
        foreach ($stritem in $stracc)
        {
            $metrics=Get-AzMetric -ResourceId $stritem.id -TimeGrain 01:00:00 -WarningAction SilentlyContinue
            $B=$B + $metrics.Data.Average
        }
        $GB=[MATH]::Round($B/1024/1024/1024,2)
        Write-Output "Total GB of storage accounts in $item" $GB >> $slide
        Write-Output "Total of App Service in $item" $appser.Name.Count >> $slide
        if ($sql -eq 1)
        {
            $count=0
            $sqlsvr=Get-AzSqlServer -ResourceGroupName $item
            foreach ($i in $sqlsvr.ServerName)
            {
                $sqldb=Get-AzSqlDatabase -ResourceGroupName $item -ServerName $i
                foreach ($db in $sqldb.DatabaseName)
                {
                    if ($db -ne 'master')
                    {
                        $count=$count+1;
                    }
                }
                
            }
            Write-Output "Total of SQL database in $item" $count >> $slide
        }
        if ($mi -eq 1)
        {
            $misql=Get-AzSqlInstance -ResourceGroupName $item
            Write-Output "Number of SQL Managed Instance in $item " $misql.Count >> $slide
        }
        #Write-Output "--------SLIDE 8---------" >> $file
        Write-Output "Number of Unused disks in $item" $unused_disk >> $slide
        $unused_nwinterface=0
        foreach ($nw_item in $nwinterface)
        {
            #Write-Output $nw_item.VirtualMachine >> $file
            if ($null -eq $nw_item.VirtualMachine)
            {
                $unused_nwinterface=$unused_nwinterface+1
            }
        }
        $unused_pubip=0
        Write-Output "Number of Unused network interfaces in $item" $unused_nwinterface >> $slide
        foreach ($pubip_item in $pubiplist)
        {
            If ($null -eq $pubip_item.IpConfiguration)
            {
                $unused_pubip=$unused_pubip+1
            }
        }
        Write-Output "Number of Unused public IP addresses in $item" $unused_pubip >> $slide
        $unused_lb=0
        foreach ($lb_item in $lblist)
        {
            if ($null -eq $lb_item.BackendAddressPools.Name)
            {
                $unused_lb=$unused_lb+1
            }
        }
        Write-Output "Number of unused Load Balancers in $item" $unused_lb >> $slide
        $unused_apgw=0
        foreach ($apgw_item in $apgwlist)
        {
            If ($null -eq $apgw_item)
            {
                $unused_apgw=$unused_apgw+1
            }
        }
        Write-Output "Number of unused Application Gateway in $item" $unused_apgw >> $slide
        Write-Output "----------------------------------------------" >> $slide
        Write-Output "----------------------------------------------" >> $slide
    }
    