import matplotlib.pyplot as plt
import csv
import sys

def slo_parse(filename):
    filepath = filename
    percentileth=[]
    latval = []
    opcode = []
    with open(filepath) as fp:
       line = fp.readline()
       cnt = 1
       while line:
           #print("Lines is: {}".format(line.strip()))
           line = fp.readline()
           linestr = line.strip().split(',')
           if len(linestr)>1 and str(linestr).find("CLEANUP")==-1:
               #print "linestr[1]:"+linestr[1]
               if "PercentileLatency" in str(linestr[1]):
                   latval.append(linestr[2])
                   percentile = str(linestr[1]).strip().split("PercentileLatency")
                   #print "percentile:"+percentile[0].replace('th','')
                   percentileth.append(percentile[0].replace('th',''))
                   opcode.append(linestr[0])
           #print len(linestr)

    #print percentileth
    #print latval

    with open("slo_parsed_output","w") as filehandle:
        opcode_test = opcode[0]
        filehandle.write('%s \n' % str(opcode[0]))
        for valPer,valLat,valop in zip(percentileth,latval,opcode):
            if valop != opcode_test:
                filehandle.write('\n %s \n' % str(valop))
                opcode_test = valop
            filehandle.write('%s,%s\n' % (str(valPer),str(valLat)))
        filehandle.close()

def slo_plot():
    x_a = []
    y_a = []
    x_b = []
    y_b = []
    operation = []
    temp = 0
    with open('slo_parsed_output','r') as fp:
        line = fp.readline()
        while line:
            linestr = line.strip().split(',')
            if str(line).find(']')!=-1:
                #print str(line)
                operation.append(str(line))
                temp = temp + 1
                #print temp
            if len(linestr)>1 and temp%2==1:
                x_a.append(float(linestr[1]))
                y_a.append(float(linestr[0]))
            elif len(linestr)>1 and temp%2==0:
                x_b.append(float(linestr[1]))
                y_b.append(float(linestr[0]))
            line = fp.readline()
    plt.plot(x_a,y_a, label=str(operation[0]))
    plt.plot(x_b,y_b, label=str(operation[1]))
    plt.xlabel('Percentile')
    plt.ylabel('time(us)')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

if __name__ == "__main__":
     if len(sys.argv)<2:
	print "Please enter file name as argument"
	exit()
     else:
        #print len(sys.argv)
        slo_parse(str(sys.argv[1]))
        slo_plot()
