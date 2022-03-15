from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.integration import SQS
from  diagrams.aws.storage import S3

def connect(a,b, *args):
    a >> b
    i = 0
    if args:
        previous = b
        for i in range(len(args)):
            current = args[i]
            previous >> current
            previous = current


with Diagram(filename="example_flow", show=False, direction="LR", outformat="pdf", graph_attr={"pad": "0.5", "fontsize": "25"}):
    elb =  ELB("load balancer")
    service1 = EC2('Service1')
    service2 = EC2('Service2')
    service3 = EC2('service3')
    db = RDS("primary DB")

    connect(elb, service1, db)
    connect(service1, db)
    connect(elb, service2, db)
    connect(service1, SQS('sqs'), service3, S3('s3'))
