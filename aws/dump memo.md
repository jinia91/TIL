# AMI

- Amazon Machine Image(AMI)는 인스턴스를 시작하는 데 필요한 정보를 제공하는 AWS에서 지원되고 유지 관리되는 이미지
- 인스턴스를 시작할 때 AMI를 지정해야 함
- 동일한 구성의 인스턴스가 여러 개 필요할 때는 한 AMI에서 여러 인스턴스를 시작할 수 있음
-  서로 다른 구성의 인스턴스가 필요할 때는 다양한 AMI를 사용하여 인스턴스를 시작할 수 있음

# EBS
> elastic block storage
<img width="983" alt="스크린샷 2023-02-10 오후 8 36 46" src="https://user-images.githubusercontent.com/85499582/218083185-a303d7cd-4bde-44e2-8b63-a72e7469ddf5.png">

https://velog.io/@realvividdream/AWS-SAA-EC2%EC%99%80-EBS

# Redshift

> 아마존 레드시프트는 더 큰 클라우드 컴퓨팅 플랫폼 아마존 웹 서비스의 일부를 형성하는 데이터 웨어하우스 제품

- 쿼리기반 
- 높은 성능
- 대규모 온라인 트랜잭션 처리


# 배치 그룹
> 단일존에서 논리적으로 묶인 ec2 그룹, 클러스터


# 허브 앤 스포크 방식 네트워크 - aws vpn cloudhub

https://docs.aws.amazon.com/ko_kr/vpn/latest/s2svpn/VPN_CloudHub.html


# route53 - elb

도메인 트래픽을 ELB 로드 밸런서로 라우팅하려면 Amazon Route 53을 사용하여 로드 밸런서를 지정하는 별칭 레코드(alias record)를 생성해야함!

- elb로 헬스체크 자동으로 해주고, nginx처럼 트래픽 분산가능

https://docs.aws.amazon.com/ko_kr/Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.html

https://developer88.tistory.com/312


# IOPS

저장장치 퍼퍼몬스 측정단위
- aws ebs는 초당 256kb이

# aws glacier and vault

https://docs.aws.amazon.com/ko_kr/amazonglacier/latest/dev/vault-inventory.html




# tip
- rds snapshot 남길때 퍼포먼스 저하가 온다
- 이중화 MuIti-AZ
- 오토스케일링 기본 할당량 : https://docs.aws.amazon.com/ko_kr/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html


# 다시보기


NEW QUESTION 27
You are setting up a VPC and you need to set up a public subnet within that VPC. Which following requirement must be met for this subnet to be considered a public subnet?
A. Subnet's traffic is not routed to an internet gateway but has its traffic routed to a virtual private gateway. B. Subnet's traffic is routed to an internet gateway.
C. Subnet's traffic is not routed to an internet gateway.
D. None of these answers can be considered a public subne
Answer: B
Explanation: A virtual private cloud (VPC) is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS cloud. You can launch your AWS resources, such as Amazon EC2 instances, into your VPC. You can configure your VPC: you can select its IP address range, create subnets, and configure route tables, network gateways, and security settings.
A subnet is a range of IP addresses in your VPC. You can launch AWS resources into a subnet that you select. Use a public subnet for resources that must be connected to the internet, and a private subnet for resources that won't be connected to the Internet.
If a subnet's traffic is routed to an internet gateway, the subnet is known as a public subnet.
If a subnet doesn't have a route to the internet gateway, the subnet is known as a private subnet.
If a subnet doesn't have a route to the internet gateway, but has its traffic routed to a virtual private gateway, the subnet is known as a VPN-only subnet. Reference: http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html



NEW QUESTION 69
Your company has been storing a lot of data in Amazon Glacier and has asked for an inventory of what is in there exactly. So you have decided that you need to download a vault inventory. Which of the following statements is incorrect in relation to Vault Operations in Amazon Glacier?
A. You can use Amazon Simple Notification Service (Amazon SNS) notifications to notify you when the job completes. B. A vault inventory refers to the list of archives in a vault.
C. You can use Amazon Simple Queue Service (Amazon SQS) notifications to notify you when the job completes.
D. Downloading a vault inventory is an asynchronous operatio




NEW QUESTION 83
You need to measure the performance of your EBS volumes as they seem to be under performing. You have come up with a measurement of 1,024 KB I/O but your colleague tells you that EBS volume performance is measured in IOPS. How many IOPS is equal to 1,024 KB I/O?
A. 16 B. 256 C. 8 D. 4

