#File Name: ns exp2.tcl
#Description: Simulating four node point-to-point network with TCP and UDP agent #################################################################################

set ns [new Simulator]

#Open a new file for NAMTRACE set nf [open out.nam w]
$ns namtrace-all $nf

#Open a new file to log TRACE set tf [open out.tr w]
$ns trace-all $tf

#Body of the 'finish' procedure proc finish {} {
global ns nf tf
$ns flush-trace close $nf close $tf
exec nam out.nam &
exit 0
}

#Create Nodes
set nO [$ns node] set nl [$ns node] set n2 [$ns node] set n3 [$ns node]

#Create Links between Nodes
$ns duplex-link $n0 $n2 1Mb lOms DropTail
$ns duplex-link $nl $n2 1Mb lOms DropTail
$ns duplex-link $n2 $n3 1Mb lOms DropTail

#Set the queue limit - default is 50 packets
$ns queue-limit $n0 $n2 50
$ns queue-limit $nl $n2 50
$ns queue-limit $n2 $n3 50

#Create TCP Agent between node O and node 3 set tcpO [new Agent/TCP]
$ns attach-agent $n0 $tcp0 set sinkO [new Agent/TCPSink]
$ns attach-agent $n3 $sink0
$ns connect $tcp0 $sink0

#Create FTP Application for TCP Agent set ftpO [new Application/FTP]
$ftp0 attach-agent $tcp0

#Specify TCP packet size Agent/TCP set packetSize 1000

#Create UDP Agent between node 1 and node 3 set udpO [new Agent/UDP]
$ns attach-agent $nl $udp0 set nullO [new Agent/Null]
$ns attach-agent $n3 $null0
$ns connect $udp0 $null0

#Create CBR Application for UDP Agent set cbrO [new Application/Traffic/CBR]
$cbr0 set packetSize 500
$cbr0 set interval 0.005
$cbr0 attach-agent $udp0

#Start and Stop FTP Traffic
$ns at 0.75 "$ftp0 start"
$ns at 4.75 "$ftp0 stop"

#Start and Stop CBR traffic
$ns at 0.5 "$cbr0 start"
$ns at 4.5 "$cbr0 stop"

#Stop the simulation
$ns at 5.0 "finish"
 

 
#Run the simulation
$ns run
