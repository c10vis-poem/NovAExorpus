# CQRS (Command Query Responsibility Segregation) Pattern with an Example | by İnci KÜÇÜK | Stackademic

Stackademic
CQRS (Command Query
Responsibility Segregation) Pattern
with an Example
İnci KÜÇÜK
Follow
6 min read · Dec 6, 2024
2
Open in app
Sign up
Sign in
Search
Write


CQRS is a software architectural pattern that separates the operations for
reading data (queries) and writing data (commands). The main principle of
CQRS is to have distinct models and mechanisms for handling command
(write) and query (read) operations. This pattern is particularly useful in
microservices architectures because it allows each type of operation
(reading and writing) to be optimized independently, leading to better
scalability, performance, and flexibility in complex systems.


LinkedIn: https://www.linkedin.com/in/inci-kucuk
GitHub: https://github.com/incikucuk
What are the core concepts of CQRS?
1. Commands (Writes):
Commands represent actions that change the state of the system. These
actions might involve creating, updating, or deleting data in the system.
Commands generally don’t return a result; they just perform an action.
For commands, the system ensures atomicity and consistency to
maintain the integrity of data. Commands are typically synchronous and
may involve complex transactional operations to guarantee that data
changes are reliable.
2. Queries (Reads):
Queries represent actions that retrieve data from the system without
changing its state. These actions focus on reading data and typically
return the requested information.
Read operations are often optimized for performance and can be
implemented using denormalized data models (i.e., data that is stored in
a way that is more efficient for querying but may have redundant data).
Why Use CQRS in Microservices?
In a microservices architecture, CQRS provides several benefits due to the
different requirements for reading and writing data. Here’s why it makes
sense to separate commands and queries:


1. Different Requirements for Read and Write Operations:
Write operations need to ensure data consistency and transaction
integrity. They often involve ACID (Atomicity, Consistency, Isolation,
Durability) properties and may need to ensure strict consistency across
the system.
Read operations are optimized for performance and speed, often
requiring denormalized data or even caching mechanisms to ensure fast
responses.
2. Why separate them? Because writing data requires strict consistency,
while reading data can be more flexible and optimized for speed.
Get İnci KÜÇÜK’s stories in your inbox
Join Medium for free to get updates from this writer.
Enter your email
Subscribe
Remember me for faster sign in
3. Optimizing Read and Write Models Independently:
Write models often work with normalized, relational databases to ensure
data consistency and integrity. These models focus on the accuracy and
correctness of updates.
Read models might be denormalized for better performance, often using
NoSQL databases or caching systems to speed up query responses. In
CQRS, the read model may also be structured in a way that allows for
faster querying, even if the underlying write model is complex.


4. Scalability of Reads and Writes:
In systems with heavy read traffic, the read model may need to be scaled
independently from the write model. For example, in an e-commerce
platform, while users may frequently view product details (read), the
number of product updates (write) is much less frequent.
With CQRS, you can scale read and write services independently to
accommodate their different traffic patterns.
5. Eventual Consistency and Asynchronous Updates:
In CQRS, especially when combined with Event Sourcing, the system
may not need to maintain immediate consistency across all services. For
instance, a write operation may create an event (such as an
“OrderPlaced” event) that updates the read model asynchronously. This
means that there may be a slight delay between the time data is written
and the time it is reflected in the read model (known as eventual
consistency).
Eventual consistency helps systems scale better and handle distributed
environments where real-time consistency isn’t a strict requirement.
Benefits of CQRS in Microservices


1. Improved Performance:
By optimizing the read and write operations independently, each
operation can be designed to perform its best. Read operations can be
highly optimized for speed (e.g., through denormalization or caching),
while write operations can ensure consistency and data integrity.
2. Independent Scalability:
Since reads and writes are handled by different models, they can be
scaled independently based on the traffic each generates. For instance, a
system with high read traffic (e.g., a search engine) can scale the query
service without needing to scale the command service.
3. Flexibility and Evolvability:
With CQRS, the system becomes more flexible because changes to one
model (read or write) do not necessarily impact the other. This is
particularly useful in large systems with complex requirements where
the read and write operations evolve at different rates.
4. Asynchronous Processing and Event-Driven Architecture:
CQRS facilitates asynchronous communication and event-driven
architectures, which allow for better responsiveness and scalability. By
handling events asynchronously, you can build a system that can respond
to high loads without blocking or waiting for real-time consistency.
How to Build this architecture? Here it’s :) CQRS Flow: Step-by-Step
1. Command Processing (Write Operations):


A User or Client initiates a write operation (e.g., placing an order).
The Command Handler processes the command and updates the Write
Model (which could be a relational database).
If Event Sourcing is used, the Event Store records the resulting events
(e.g., “OrderPlaced”).
2. Event Propagation:
After a command is processed, an Event is triggered and placed on the
Event Bus.
The Event Bus transmits these events to the read side, which may update
the Read Model based on the event.
3. Query Processing (Read Operations):
When the system needs to handle read operations (e.g., fetching an
order’s details), a Query Handler is invoked.
The Query Handler retrieves data from the Read Model, which is
optimized for fast retrieval, often using a NoSQL database or cache to
store denormalized, query-friendly data.
4. Data Synchronization:
The Event Bus ensures eventual consistency between the Write Model
and the Read Model. As events are published, the read side is eventually
updated, but not necessarily in real-time. This leads to eventual
consistency, where the read model might be slightly out-of-sync with the
write model at any given time.


CQRS Diagram Explanation
CQRS is a pattern that splits the handling of write operations (commands)
and read operations (queries) into separate models, which can be optimized
independently. The key idea behind CQRS is to separate the responsibilities
of command and query processing to handle each with the most appropriate
design, enhancing performance, scalability, and flexibility. This approach
works particularly well in microservices architectures.
Here’s how the components of a CQRS system would typically interact,
visualized in a basic diagram format:
+------------------+           +-------------------------+           +----------
|      User        |  ----->   |    Command Handler      |  ----->   |   Write M
|    (Client)      |           |  (Process Commands)      |           |     (SQL
+------------------+           +-------------------------+           +----------
                                               |
                                         +-------------------+
                                         |    Event Store    |
                                         |  (Event Sourcing) |
                                         +-------------------+
                                               |
                                     +------------------------+
                                     |        Event Bus       |
                                     +------------------------+
                                               |
+---------------------+         +-------------------------+         +-----------
|   Query Handler     |  <----> |      Read Model         |  <----> |  NoSQL DB 
|   (Process Queries) |         |   (Denormalized Data)   |         |   (Fast Ac
+---------------------+         +-------------------------+         +-----------
                                               |
                                        +--------------+
                                        |    User      |
                                        |   (Client)   |
                                        +--------------+


Components in the Diagram:
1. Command Handler: Handles write operations (commands) and updates
the system state by modifying the write model.
2. Event Store: Stores events that are generated after commands are
executed. These events represent state changes in the system.
3. Event Bus: Acts as the mediator for communication between the write
side and the read side. Events are passed through the event bus and
consumed by the read model to update the read side.
4. Query Handler: Handles read operations and fetches data from the read
model.
5. Read Model: Optimized for read access, typically denormalized for faster
querying, and stored in systems like NoSQL databases or caches.
6. NoSQL DB / Cache: The data store used for fast read access, providing
quick responses to queries by utilizing denormalized data and caching
mechanisms.
Congratulations !, I hope to work :)
I hope it will be useful for you. :)
Don’t forget to follow me, your support and feedback are very important for me,
Thanks..
LinkedIn: https://www.linkedin.com/in/inci-kucuk
GitHub: https://github.com/incikucuk
Delightful encodings!


Stackademic 🎓
Thank you for reading until the end. Before you go:
Please consider clapping and following the writer! 👏
Follow us X | LinkedIn | YouTube | Discord | Newsletter | Podcast
Create a free AI-powered blog on Differ.
More content at Stackademic.com
Cqrs Pattern
Microservice Architecture
Microservices
Architecture
Software
Published in Stackademic
86K followers · Last published 2 hours ago
Stackademic is a learning hub for programmers, devs, coders, and engineers.
Our goal is to democratize free coding education for the world.
Follow
Written by İnci KÜÇÜK
30 followers · 41 following
Java Full Stack Developer | Software Engineer | incikucuk98@gmail.com |
https://www.linkedin.com/in/inci-kucuk | https://github.com/incikucuk | Please
follow me
Follow




