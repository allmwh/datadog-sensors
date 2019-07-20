#!/usr/bin/env python
# coding: utf-8




from plumbum.cmd import sensors
from datadog_checks.checks import AgentCheck





class sensor(AgentCheck):
    def check(self, instance):
        read = sensors
        read = read()
        read = read.split('\n')
        
        for line in read:
            if line.startswith('Core'):
                line=line.split()
                #print(line[0]+" "+line[1]+line[2][1:5])
                self.gauge('sensor.' + line[0]+' '+line[1], float(line[2][1:5]))







