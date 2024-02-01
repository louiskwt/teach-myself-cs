# Computer Organization And Design (RISC-V)


## Notes Index




## Chapter 1

**Progress**

The rapid advance of processors and computer technology has yielded a tremendous progress in society and made computers omipresent in our life.

- Notable ideas

    1. computer system in cars thanks to the advance in multiprocessor
	2. the web (and social media)
	3. search engine
	4. smartphones
	5. AI
	6. human genome project 

But then, my question is can the progress made in computation spread and elevate other domains as well. Yes, automobiles and some consumer technologies have got better, but in some fields such as education and transportation, I don't think the advance in comptation has not been utilised to its full potential due to some constraints (maybe energy and other human factors)

**Three-class of Computing and Applications**

- PC (personal computers)

    - delivering good performance to a single user at a low cost 
	- it runs third-party softwares
	- it's controlled using a graphical interface as well as some IO devices such as a keyboard or mouse

- Servers

	- a computer used for running larger programs or various jobs
	- it serves multiple users often simultaneously
	- can be accessed only through a network
	- higher emphasis on dependability (achieved through redundency)
	- a crash can be more costly than than for PC
	- supercomputer is a on the high end and extreme side of server

- embedded computers
	
	- a computer integrated into another physical device 
	- used for running one predetermined application or a collection of software
	- can be found in car, train, plane and home appliances
	- a crash can be upsetting, devastating and extremely costly
	- dependability is achived through simplicity (doing a small set of jobs perfectly)

- Intersting tibit

	- TB vs TiB
	> Originally 1,099,511,627,776 (2^40) bytes, although communications and secondary storage systems developers started using the term to mean 1,000,000,000,000 (10^12) bytes. To reduce confusion, we now use the term tebibyte (TiB) for 2^40 bytes, defining terabyte (TB) to mean 10^12 bytes.

	- apparently, TB is 21% less than TiB, GB is 7% less than Gib, MB is 5% less than Mib

**Post-PC Era**

- The rise of PMC (Personal Mobile Device)

	- PMC are battery operated with wireless connectivity to the internet and typically only hundreds of dollars 
	- users can download apps and run it on the device
	- unlike PC, it is controlled using a touch-senstive screen instead of a keyboard and mouse

- Cloud computing replacing servers

	- large tech companies (AWC and Google) take over traditional servers by building Warehouse Scale Computers (WSC) 
	- this leads to SaaS becuase it lowers the cost of computation for the server since they can rent the infrastructure from WSC providers
	- Formal definition:

		> large collections of servers that provide services over the Internet; some providers rent dynamically varying numbers of servers as a utility.

- The advance of Multiprocessor

	- in the 60s and 70s, a primary constraint on computer performance is memory space
	- thus there's only one rule for programmers: minimize memory space to make things fast
	- but things have changed with the advances in computer design and memory technology
	- a new constraint: the parallel nature of processors and the hierarchical nature of memories and how to take advantage of them

- The number of embedded processors sold every year greatly outnumbers the number of PC and even post-PC processors?

	- by just counting the number of embedded devices at home, it seems that I'm surrounded by them without actually knowing
	- Some stat from Dell
		>  The industry sold 349 million PCs in 2021 and 31 billion microprocessors, meaning 98.9% went into non-PC devices. 

- Where each of the following is the right place to look for a performance bottleneck?

	- The algorithm chosen --> the software is slow at performing a specific task
	- The programming language or compiler --> the build time of a progarm is slow and some functions (like concurrency) are not supported 
	- The operating system --> I/O operations are slow
	- The processor --> the number of instructions and the memory needed to perform the operation are huge
	- The I/O system and devices --> Porting a PC software to PMD 

**Questions Ahead**

- How are programs written in a high-level language, such as C or Java, translated into the language of the hardware, and how does the hardware execute the resulting program?

- What is the interface between the software and the hardware, and how does software instruct the hardware to perform needed functions?

- What determines the performance of a program, and how can a programmer improve the performance?

- What techniques can be used by hardware designers to improve performance?

- What are the reasons for and the consequences of the recent switch from sequential processing to parallel processing?

**Eight Great Ideas in Computer Architecture**

1. Design for Moore's Law

	- Moore's Law states that the integrated circuit resources double every 18-24 months
	- computer architects must anticipate where the technology will be when the design finishes rather than design for where it starts
	- this is because the resouces available per chip can easily double or quadruple between start and finish

2. Use Abstraction to Simplify Design

	- this is more of a productivity technique
	- lower-level details are hidden to offer a simpler model at higher levels

3. Make the common case fast

	- Making the common case fast will tend to enhance performance better than optimizing the rare case
	- the common case is often simpler than the rare case and hence is easier to enhance
	- this common sense advice implies that you know what the common case is which is only possible with careful experimentation and measurement

4. Performance via parallelism

	- computer architects have offered designs that get more performance by computing operations in parallel

5. Performance via pipelining

	- a particular pattern of parallelism
	- chaining up the operations in small parts

6. Performance via Prediction

	- it can be faster on average to guess and start working rather than wait uintil you know for sure
	- assuming that the mechanism to recover from a misprediction is not too expensive and your prediction is relatively accurate

7. Hierarchy of Memories

	- the fastest, smallest, and the most expensive memory per bit at the top
	- the slowest, largest, and the least expensive memory per bit at the bottom
	- caches give the programmer the illusion that main memory is almost as fast as the top of the hierarchy and nearly as big and cheap as the bottom of the hierarchy
	- this has to do with cost and performance

8. Dependability via redundancy

	- including redundant components that can take over when a failure occurs and to help detect failures 

**Below your program**

- Sysyem softwres

	- Software that provides services that are commonly useful, including operating systems, compilers, loaders, and assemblers.

- Operating System

	- nterfaces between a user’s program and the hardware and provides a variety of services and supervisory functions.
	- Functions

		1. handling basic input and output operations
		2. allocating storage and memory
		3. providing for protected sharing of the computer among multiple application using it simultaneously

- Compliers 

	-  the translation of a program written in a high-level language, such as C, C++, Java, or Visual Basic into instructions that the hardware can execute

- Assembly langauge

	- a symbolic representation of computer instructions

- machine language

	- a binary langauge that the machine understands

- high-level langauges

	- A portable language such as C, C++, Java, or Visual Basic that is composed of words and algebraic notation that can be translated by a compiler into assembly language.

**Five classic components of a computer**

1. Inputing
2. Outputing
3. Storing data
4. Data path (CPU)
5. control (CPU)

**Computer Parts**

- The integrated circuit board

	- also called a chip. 
	- a device that combines dozens to millions of transistors

- CPU

	- Also called processor. 
	- The active part of the computer, which contains the datapath and control and which adds numbers, tests numbers, signals I/O devices to activate, and so on.

- Data path

	- The component of the processor that performs arithmetic operations.
	- it includes the ALU + registers + buses and control units

- Control

	- The component of the processor that commands the datapath, memory, and I/O devices according to the instructions of the program.

- DRAM

	- Memory built as an integrated circuit; it provides random access to any location. Access times are 50 nanoseconds and cost per gigabyte in 2012 was $5 to $10.
	- the main source of memory for your device
	- it sits at the top of the memory hierarchy

- Cache Memory

	- A small, fast memory that acts as a buffer for a slower, larger memory
	- aka: a safe place to hide staff


- Instruction set architecture

	- An abstract interface between the hardware and the lowest-level software that encompasses all the information necessary to write a machine language program that will run correctly, including instructions, registers, memory access, I/O, and so on.

	- An instruction set architecture allows computer designers to talk about functions independently from the hardware that performs them.

- Application Binary Interface (ABI)

	- The user portion of the instruction set plus the operating system interfaces used by application programmers. It defines a standard for binary portability across computers.
	

- Implementation

	- an implementation is hardware that obeys the architecture abstraction
	- Both hardware and software consist of hierarchical layers using abstraction, with each lower layer hiding details from the level above.
	- One key interface between the levels of abstraction is the instruction set architecture—the interface between the hardware and low-level software. This abstract interface enables many implementations of varying cost and performance to run identical software.

**Communicating with Other Computers**

- Major advantages of networked computer 

	1. high-speed communication
	2. Resources sharing via sharing I/O devices
	3. non-local access

- Networks vary in length and performance, with the cost of communication increasing according to both the speed of communication and the distance that information travels.

- Ethernet (Local area network / LAN)

	- Local area networks are interconnected with switches that can also provide routing services and security.

- Wide area networks 

	- A network extended over hundreds of kilometers that can span a continent
	- it can be used to connect LAN by ISP


