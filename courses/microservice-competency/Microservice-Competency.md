# Microservice Competency

## Section 1: Introduction to REST Microservices

### What Are Microservices?
Microservices architecture is an approach to software design where a single application is composed of small, independent services. Each service runs its own process and communicates with other services via HTTP/HTTPS, usually using RESTful APIs. This contrasts with monolithic architectures, where all functionalities are interwoven into a single program.

### What is REST?
REST stands for Representational State Transfer. It's not a standard or protocol but an architectural style for designing networked applications. Here are the key principles of REST:

**Stateless:** Each request from client to server must contain all the information needed to understand and process the request. The server doesn't store any information about the client's state between requests.
Resource-Based: Everything in REST is a resource (e.g., users, products). Each resource is identified by a unique URL.
**Client-Server:** The architecture separates the user interface (client) from the data storage and services (server). This separation improves portability of the user interface across multiple platforms.
**Cacheable:** Responses from the server can be cached to reduce client-server communication.
**Uniform Interface:** REST services use standard HTTP methods like GET, POST, PUT, DELETE for all operations. This uniformity simplifies the architecture.

## REST in Microservices
When integrating REST with microservices:

**Decoupling:** Each service can be developed, tested, and deployed independently due to the stateless nature of REST.
**Scalability:** Services can scale independently based on demand.
**Flexibility:** Different services can be written in different programming languages or use different data storage solutions.
**Discovery and Communication:** Services often need a service discovery mechanism to find each other, and might use API gateways for managing requests.

## Basic REST Operations in Microservices
**GET:** Retrieve a resource or data. For example, GET /users/1 might retrieve details of user with ID 1.
**POST:** Create a new resource. POST /users could create a new user.
**PUT:** Update a resource. PUT /users/1 might update details for user 1.
**DELETE:** Remove a resource. DELETE /users/1 would delete user 1.
**PATCH:** Partially update a resource, unlike PUT which might replace the entire resource.

## Challenges of REST Microservices
**Complexity:** Managing many services can become complex, especially concerning service discovery, data consistency, and debugging.
**Network Latency:** Since services communicate over the network, there can be latency issues.
**Data Management:** Ensuring data integrity across services without a centralized database can be challenging.

## Tools and Technologies
For developing REST microservices, you might use:

**Frameworks:** Spring Boot for Java, **FastAPI, Flask, Django for Python**, Express.js for Node.js.
**Service Discovery:** Tools like Consul or Kubernetes' built-in discovery.
**API Gateways:** TODO: Ask Jey about API gateway alternatives
**Monitoring:** Tools like Prometheus and Grafana for observability.

## Assignment
Create a simple REST api that manages a single data entity: `Customer`

- Create a webserver
- Use
