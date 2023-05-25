#File Name: ns exp4.tcl
#Description: transmission of ping messaged over a network topology ###################################################################

#Create a simulator object set ns [new Simulator]

#Open a trace file
set nf [open out.nam w]
$ns namtrace-all $nf

#Define a 'finish' procedure proc finish {} {
global ns nf
$ns flush-trace close $nf
exec nam out.nam &
exit 0
}

#Create three nodes set n0 [$ns node] set nl [$ns node] set n2 [$ns node]

#Connect the nodes with two links
$ns duplex-link $n0 $nl 1Mb l0ms DropTail
$ns duplex-link $nl $n2 1Mb l0ms DropTail
#Define a 'recv' function for the class 'Agent/Ping' Agent/Ping instproc recv {from rtt} {
$self instvar node
puts "node [$node id] received ping answer from\
$from with round-trip-time $rtt ms."
}

#Create two ping agents and attach them to the nodes nO and n2 set pO [new Agent/Ping]
$ns attach-agent $n0 $p0

set pl [new Agent/Ping]
$ns attach-agent $n2 $pl

#Connect the two agents
$ns connect $p0 $pl

#Schedule events
$ns at 0.2 "$p0 send"
$ns at 0.4 "$pl send"
$ns at 0.6 "$p0 send"
$ns at 0.6 "$pl send"
$ns at 1.0 "finish"

#Run the simulation
$ns run
