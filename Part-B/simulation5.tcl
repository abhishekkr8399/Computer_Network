#File Name: ns exp5.tcl
#Description: Simulate an Ethernet LAN using N-nodes (6 10) ######################################################################


set ns [new Simulator]

#Open a new file for NAMTRACE set nf [open out.nam w]
$ns namtrace-all $nf

#Open a new file to log TRACE set tf [open out.tr w]
$ns trace-all $tf

#Body of the finish procedure proc finish{} {
global ns nf tf
$ns flush-trace close $nf
close $tf
exec nam out.nam &
exit 0
}

#Create Nodes set n0 [$ns node] set nl [$ns node] set n2 [$ns node] set n3 [$ns node] set n4 [$ns node] set nS [$ns node] set n6 [$ns node] set n7 [$ns node] set n8 [$ns node] set n9 [$ns node]
set nl0 [$ns node]

#Create a Local Area Network (LAN) of 10 Nodes
$ns make-lan "$n0 $nl $n2 $n3 $n4 $n5 $n6 $n7 $n8 $n9 $n10" 100Mb 1ms LL Queue/DropTail Mac/802 3

#Create TCP Agent between node 0 and node 3 set tcp0 [new Agent/TCP]
$ns attach-agent $n0 $tcp0 set sinkO [new Agent/TCPSink]
$ns attach-agent $n3 $sink0
$ns connect $tcp0 $sink0

#Create FTP Application for TCP Agent set ftpO [new Application/FTP]
$ftp0 attach-agent $tcp0

#Specify TCP packet size Agent/TCP set packetSize 1000

#Start and Stop FTP Traffic
$ns at 0.75 "$ftp0 start"
$ns at 4.75 "$ftp0 stop"

#Stop the simulation
$ns at 5.0 "finish"

#Run the simulation
$ns run
