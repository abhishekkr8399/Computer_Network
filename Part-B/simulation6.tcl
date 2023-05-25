#File Name: ns exp6.tcl
#Description: Simulate an Ethernet LAN and set multiple traffic nodes ######################################################################

set ns [new Simulator]

#Open a new file for NAMTRACE set nf [open out.nam w]
$ns namtrace-all $nf

#Open a new file to log TRACE set tf [open out.tr w]
$ns trace-all $tf

#Body of the 'finish' procedure proc finish{} {
global ns nf tf
$ns flush-trace close $nf
close $tf
exec nam out.nam &
exit 0
}

#Create Nodes set no [$ns node] set nl [$ns node] set n2 [$ns node] set n3 [$ns node] set n4 [$ns node] set n5 [$ns node] set n6 [$ns node] set n7 [$ns node] set n8 [$ns node] set n9 [$ns node]

#Create a Local Area Network (LAN) of 10 Nodes
$ns make-lan "$n0 $nl $n2 $n3 $n4 $n5 $n6 $n7 $n8 $n9" 100Mb 1ms LL Queue/DropTail Mac/802 3

#Create TCP Agent between node 0 and node 3 set tcp0 [new Agent/TCP]
$ns attach-agent $n0 $tcp0
set sink0 [new Agent/TCPSink]
$ns attach-agent $n3 $sink0
$ns connect $tcp0 $sink0

#Create FTP Application for TCP Agent set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0

#Specify TCP packet size Agent/TCP set packetSize 1000

#Create TCP Agent between node 1 and node 3 set tcpl [new Agent/TCP]
$ns attach-agent $nl $tcpl set sinkl [new Agent/TCPSink]
$ns attach-agent $n3 $sinkl
$ns connect $tcpl $sinkl

#Create Telnet Application for TCP Agent set telnet0 [new Application/Telnet]
$telnet0 set interval 0.005
$telnet0 attach-agent $tcpl

#Start and Stop FTP Traffic
$ns at 0.75 "$ftp0 start"
$ns at 4.75 "$ftp0 stop"

#Start and Stop Telnet traffic
$ns at 0.5 "$telnet0 start"
$ns at 4.5 "$telnet0 stop"

#Stop the simulation
$ns at 5.0 "finish"

#Run the simulation
$ns run
