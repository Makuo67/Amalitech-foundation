# Design and Evaluate an AWS Solution Using the Well-Architected and Cloud Adoption Frameworks

## Review the Existing Architecture

### Components of the Workload

- Frontend Web Tier running on on-premises servers (serving HTML/CSS/JS).

- Backend Database Tier (relational DB: PostgreSQL).

Networking using on-prem firewall and routing.

- User Access Layer (browser → on-prem server).

- Basic monitoring (assumed manual or limited).

- Manual backups or potentially none.

### Potential Risks / Weaknesses

- Single-AZ style deployment (no high availability).

- No automated backup or disaster recovery strategy.

- Security groups/firewall rules may be broad or unvetted.

- Manual scaling: no auto-scaling capability.

- No encryption at rest or in transit (common in legacy systems).

- Limited observability logs, metrics, and alerts.

## AWS Well-Architected Framework Evaluation

### WAF Assessment Table

| **Pillar**                 | **Observation**                                               | **Improvement Recommendation**                                  | **Supporting AWS Service**                               |
| -------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------- |
| **Operational Excellence** | Manual deployments and reactive monitoring                    | Implement CI/CD pipeline, centralized logging, automated alerts | AWS CloudFormation, AWS CodePipeline, Amazon CloudWatch  |
| **Security**               | No encryption, broad access rules, weak IAM governance        | Enforce least-privilege IAM, enable encryption, restrict access | AWS IAM, AWS KMS, AWS WAF, AWS Shield, Security Groups   |
| **Reliability**            | Single-AZ deployment, no backups                              | Use Multi-AZ deployments, automated backup and failover         | Amazon RDS Multi-AZ, Elastic Load Balancer, AWS Route 53 |
| **Performance Efficiency** | Static content served from servers, no caching or autoscaling | Add CDN, caching layer, and autoscaling                         | Amazon CloudFront, Amazon ElastiCache, AWS Auto Scaling  |
| **Cost Optimization**      | Over-provisioned servers, no demand-based scaling             | Implement autoscaling, right-sizing, reserved instances         | AWS Auto Scaling, AWS Trusted Advisor, Amazon S3         |

## AWS Cloud Adoption Framework (CAF) Readiness

#### Business Perspective

The organization is motivated to migrate to AWS for improved scalability, availability, and cost efficiency. From a business standpoint, leadership must define clear KPIs such as reduced downtime, faster deployments, and cost savings. A financial model should compare current on-prem CapEx with AWS OpEx. Business stakeholders must align cloud adoption with overall digital transformation goals, such as faster product delivery or expanding user reach. Executive sponsorship will be crucial to create momentum and remove organizational blockers. A migration business case and ROI analysis must be developed, demonstrating tangible benefits (e.g., reduced IT maintenance). Clear communication strategies should explain how the cloud will support innovation and long-term competitiveness.

#### People Perspective

Cloud migration requires new skills for operations, development, and security teams. Staff must be trained on AWS fundamentals, automation, and DevOps practices. Existing roles may need restructuring—system admins transition into cloud engineers, DBAs into cloud database specialists, and developers into full DevOps contributors. A talent-growth plan using certification pathways will ensure workforce readiness. Change management processes should support employees through the transition and reduce resistance. Cross-functional teams should be established to encourage collaboration between development, operations, and security.

### Governance Perspective

The organization needs governance structures that align cloud usage with business value and compliance. FinOps practices must be introduced to manage cloud spending. Policies for tagging, resource provisioning, access management, and budgeting must be clearly documented. AWS Cloud Governance tools such as Control Tower and Service Catalog can standardize provisioning. Risk management frameworks must be updated to include cloud-specific risks. Governance should ensure compliance with regulatory standards (GDPR, HIPAA, etc. depending on industry).

### Platform Perspective

The platform foundation should include secure networks, standardized compute patterns, and managed database services. A well-designed landing zone using VPCs, subnets, IAM, and security controls should be provisioned. The two-tier application should be architected using EC2 or containerized with ECS/EKS, paired with RDS for the database. Infrastructure as Code (IaC) should be adopted to ensure consistency and repeatability. Monitoring and logging must be centralized. 5. Security Perspective
Security posture must shift to a shared responsibility model. Identity and access management must follow least privilege. Encryption, logging, and automated threat detection using GuardDuty or Security Hub should be implemented. Network controls should enforce the principle of zero trust. Compliance requirements need mapping to AWS services. Incident response runbooks should be created and automated where possible.

### Operations Perspective

Cloud operations should focus on automation, observability, and resilience. Monitoring, logging, patching, and scaling must be automated. CloudWatch dashboards and alarms will improve visibility. A DevOps culture should be encouraged to streamline releases and operations. Runbooks and playbooks should guide incident response. Regular game days should test operational readiness.

## Improved Architecture Design

### Revised AWS Architecture

#### Frontend Tier:

- Deployed on Amazon EC2 Auto Scaling Group behind an Application Load Balancer.

- Static assets stored and served via Amazon S3 + CloudFront.

#### Backend Tier:

- Database migrated to Amazon RDS Multi-AZ (MySQL/PostgreSQL).

- Automated backups, snapshots, and read replicas enabled.

#### Networking

- VPC with public/private subnets across at least two AZs.

- NAT Gateway for outbound traffic.

- Security groups with least-privilege rules.

#### Security

- IAM roles with least privilege.

- KMS for encryption at rest (S3, RDS, EBS).

- WAF and Shield for web protection.

#### Operations

- CloudWatch logs, events, metrics, and alarms.

- CI/CD pipeline using CodePipeline, CodeBuild, CodeDeploy.

- Infrastructure as Code using CloudFormation or Terraform.

## Reflection

This lab improved my understanding of how AWS best practices guide cloud migration decisions. Using the Well-Architected Framework forced me to evaluate the workload from multiple angles, especially security, reliability, and cost efficiency. The CAF perspectives helped me think beyond technology by considering organizational readiness, people skills, governance, and operational maturity. Designing the improved architecture demonstrated how AWS services work together to create a secure, scalable, and cost-effective environment. The exercise reinforced the importance of automation, monitoring, and least-privilege access. I learned how to justify architectural decisions using structured frameworks and how to balance technical and organizational considerations when planning cloud adoption.
