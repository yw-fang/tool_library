# check he idle CPUs in each node in the general partition in hyperion
sinfo --Node --long | grep 'general*' | awk '{print $1, $5, $6}' | while read node cpus state; do echo -n "$node "; squeue -h -w $node | wc -l; done | awk '{print $1, $2-$3}'

