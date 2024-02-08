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


**Question**

- Semiconductor DRAM memory, flash memory, and disk storage differ significantly. For each technology, list its volatility, approximate relative access time, and approximate relative cost compared to DRAM.

	- DRAM 
		- volatile
		- 50 ns
		- $0.2 per gigabyte in 2024
	
	- Flash memory
		- non-volatile 
		- 5-50 microseconds
		- $0.09 per gigabits
		- costs 45% of a DRAM

	- magnetic disk / hard disk
		- non-volatile
		- 5-20 milliseconds 
		- $0.0017 per gigabits
		- costs 0.85% of a DRAM

**Technology For Building Processors and Memory**

- Transistor

	- An on/off switch controlled by an electric signal
	- built by silicon

- Very large-scale integrated (VLSI) circuit

	- A device containing hundreds of thousands to millions of transistors.

- Semiconductor 

	- a substance that does not conduct electricty well
	- silicon is one

With a special chemical process, it is possible to add materials to silicon that allow tiny areas to transform into one of three devices:

	1. Excellent conductors of electricity (using either microscopic copper or aluminum wire)

	2. Excellent insulators from electricity (like plastic sheathing or glass)

	3. Areas that can conduct or insulate under specific conditions (as a switch) <-- transistor falls into this category

- Why chips have to be smaller and smaller to pump up the volumne

	- A key factor in determining the cost of an integrated circuit is volume.

		1. With high volumes, the manufacturing process can be tuned to a particular design, increasing the yield.

		2. The masks used to make the chip are expensive, so the cost per chip is lower for higher volumes.

		3. Engineering development costs are high and largely independent of volume; thus, the development cost per die is lower with high-volume parts.


**Performance**

- Designing Performance

	- response time
		
		- aka execution time

		- the time between the start and completion of a task including disk accesses, memory access, I/O activities, operating system over-head, cpu execution time and so on
	
		- this's what a user would be interested in
	
	- thoughput or bandwidth

		- the total amount of work done in a given time

- General point: Decreasing response time almost always improves throughput.

- Special point

> If, however, the demand for processing in the second case was almost as large as the throughput, the system might force requests to queue up. In this case, increasing the throughput could also improve response time, since it would reduce the waiting time in the queue. Thus, in many real computer systems, changing either execution time or throughput often affects the other.

- Measuring Performance

	-reponse time / wall clock time
		-  the total time to complete a task, including disk accesses, memory accesses, input/output (I/O) activities, operating system overhead—everything.

	- CPU Time

		- The actual time the CPU spends computing for a specific task.

	- user CPU Time
		- The CPU time spent in a program itself.
	
	- system CPU time
		- The CPU time spent in the operating system performing tasks on behalf of the program.

- formula

	- 1 / execution time

- Understanding Performance

	> Many applications, especially those running on servers, depend as much on I/O performance, which, in turn, relies on both hardware and software. Total elapsed time measured by a wall clock is the measurement of interest. In some application environments, the user may care about throughput, response time, or a complex combination of the two (e.g., maximum throughput with a worst-case response time).

	> To improve the performance of a program, one must have a clear definition of what performance metric matters and then proceed to find performance bottlenecks by measuring program execution and looking for the likely bottlenecks.

- Hardware's discrete time intervals

	- clock cycle

		- The time for one clock period, usually of the processor clock, which runs at a constant rate.
	
	- clock rate

		- the inverse of the clock period. (e.g. 4GHz)
	
	- clock period

		- The length of each clock cycle.

- Question 

1. Suppose we know that an application that uses both personal mobile devices and the Cloud is limited by network performance. For the following changes, state whether only the throughput improves, both response time and throughput improve, or neither improves.

	- An extra network channel is added between the PMD and the Cloud, increasing the total network throughput and reducing the delay to obtain network access (since there are now two channels).

		-  both response time and throughput improve
	
	- The networking software is improved, thereby reducing the network communication delay, but not increasing throughput.
		
		- only the latency (response time improve) 
	
	-  More memory is added to the computer

		- neither improves

2. Computer C’s performance is four times as fast as the performance of computer B, which runs a given application in 28 seconds. How long will computer C take to run that application?

	- 7 seconds

**CPU performance and Its Factor**

- A simple formula relates the most basic metrics (clock cycles and clock cycle time) to CPU time:

	> CPU execution time for a program = CPU clock cycle for a program * Clock cycle time

- Alternatively, because clock rate and clock cycle time are inverses

	> CPU execution time for a program = CPU clock cycles for a program / clockrate

- The implications of the formula

	> This formula makes it clear that the hardware designer can improve performance by reducing the number of clock cycles required for a program or the length of the clock cycle. As we will see in later chapters, the designer often faces a trade-off between the number of clock cycles needed for a program and the length of each cycle. Many techniques that decrease the number of clock cycles may also increase the clock cycle time.


- Instruction performance

	- the number of clock cycles required for a program can be written as

		> CPU clock cycles = insturction for a program * avg clock cycles per instruction

	- Clock cycles per instruction (CPI)
		
		- Average number of clock cycles per instruction for a program or program fragment.

- Classic perfromance equation

	> CPU Time = Instruction count * CPI * Clock cycle time
	> CPU Time = Instuction count * CPI / Clock rate
	> CPU Clock cycle = sum(CPI * Instuction count)

- Big Picture

	> Always bear in mind that the only complete and reliable measure of computer performance is time. For example, changing the instruction set to lower the instruction count may lead to an organization with a slower clock cycle time or higher CPI that offsets the improvement in instruction count. Similarly, because CPI depends on the type of instructions executed, the code that executes the fewest number of instructions may not be the fastest.

	- instruction mix

		- A measure of the dynamic frequency of instructions across one or many programs.

- Program performance

|Component                   |Affect what                       |How           |
|----------------------------|----------------------------------|--------------|
| Algorithm  		         | Instruction count, CPI           | The algorithm determines the number of source program instructions executed and hence the number of processor instructions executed. The algorithm may also affect the CPI, by favoring slower or faster instructions. For example, if the algorithm uses more divides, it will tend to have a higher CPI. 					  |
| Programming language       |Instruction count, CPI            |The programming language certainly affects the instruction count, since statements in the language are translated to processor instructions, which determine instruction count. The language may also affect the CPI because of its features; for example, a language with heavy support for data abstraction (e.g., Java) will require indirect calls, which will use higher CPI instructions.  |
|Complier 			         | Instruction count, CPI           | The efficiency of the compiler affects both the instruction count and average cycles per instruction, since the compiler determines the translation of the source language instructions into computer instructions. The compiler’s role can be very complex and affect the CPI in varied ways.|
|Instruction Set Architecture|Instruction count, clock rate, CPI| The instruction set architecture affects all three aspects of CPU performance, since it affects the instructions needed for a function, the cost in cycles of each instruction, and the overall clock rate of the processor.|

- Special Note

	- Although clock cycle time has traditionally been fixed, to save energy or temporarily boost performance, today’s processors can vary their clock rates, so we would need to use the average clock rate for a program. For example, the Intel Core i7 will temporarily increase clock rate by about 10% until the chip gets too warm. Intel calls this Turbo mode.

- Question

	> A given application written in Java runs 15 seconds on a desktop processor. A new Java compiler is released that requires only 0.6 as many instructions as the old compiler. Unfortunately, it increases the CPI by 1.1. How fast can we expect the application to run using this new compiler? Pick the right answer from the three choices below:

	execution time = 15s
	instuction count = I * 0.6
	CPI = +1.1

	- Ans: 15 * 0.6 * 1.1 = 9.9s


**Power Wall**

- The dominant technology for integrated circuits is called CMOS (complementary metal oxide semiconductor)

- For CMOS, the primary source of energy consumption is so-called dynamic energy—that is, energy that is consumed when transistors switch states from 0 to 1 and vice versa. The dynamic energy depends on the capacitive loading of each transistor and the voltage applied:

> Although dynamic energy is the primary source of energy consumption in CMOS, static energy consumption occurs because of leakage current that flows even when a transistor is off. In servers, leakage is typically responsible for 40% of the energy consumption. Thus, increasing the number of transistors increases power dissipation, even if the transistors are always off. A variety of design techniques and technology innovations are being deployed to control leakage, but it’s hard to lower voltage further.


> Power is a challenge for integrated circuits for two reasons. First, power must be brought in and distributed around the chip; modern microprocessors use hundreds of pins just for power and ground! Similarly, multiple levels of chip interconnect are used solely for power and ground distribution to portions of the chip. Second, power is dissipated as heat and must be removed. Server chips can burn more than 100 watts, and cooling the chip and the surrounding system is a major expense in warehouse scale computers

**The Switch from Uniprocessors to Multiprocessors**

- Rather than continuing to decrease the response time of one program running on the single processor, as of 2006 all desktop and server companies are shipping microprocessors with multiple processors per chip, where the benefit is often more on throughput than on response time.

- To reduce confusion between the words processor and microprocessor, companies refer to processors as “cores,” and such microprocessors are generically called multicore microprocessors. Hence, a “quadcore” microprocessor is a chip that contains four processors or four cores.

- Implications for programmers

> In the past, programmers could rely on innovations in hardware, architecture, and compilers to double performance of their programs every 18 months without having to change a line of code

> Today, for programmers to get significant improvement in response time, they need to rewrite their programs to take advantage of multiple processors. Moreover, to get the historic benefit of running faster on new microprocessors, programmers will have to continue to improve the performance of their code as the number of cores increases.

> Forcing programmers to be aware of the parallel hardware and to rewrite their programs to be parallel had been the “third rail” of computer architecture, for companies in the past that depended on such a change in behavior failed. From this historical perspective, it’s startling that the whole IT industry has bet its future that programmers will finally successfully switch to explicitly parallel programming.

- Challenges for programmers writing parallel programs

	1. The first reason is that parallel programming is by definition performance programming, which increases the difficulty of programming. Not only does the program need to be correct, solve an important problem, and provide a useful interface to the people or other programs that invoke it; the program must also be fast.

	2. The second reason is that fast for parallel hardware means that the programmer must divide an application so that each processor has roughly the same amount to do at the same time, and that the overhead of scheduling and coordination doesn’t fritter away the potential performance benefits of parallelism.

**Benchmark vs Workload**

- 2 Metrics for measuring performance of a processor/computer

	1. workload
	2. benchmark

- Workload

	- A set of programs run on a computer that is either the actual collection of applications run by a user or constructed from real programs to approximate such a mix. A typical workload specifies both the programs and the relative frequencies.

- Benchmark

	- A program selected for use in comparing computer performance.

- SPECratios as an indicator of performance 

	- the bigger numeric results indicate faster performance

**Fallacies and Pitfalls**

- Amdahl’s Law

	> A rule stating that the performance enhancement possible with a given improvement is limited by the amount that the improved feature is used. It is a quantitative version of the law of diminishing returns.

	- exe time after imp = exe time affected by imp / amount of imp + exe time unaffected

- Fallacy: Designing for performance and designing for energy efficiency are unrelated goals.

	> Since energy is power over time, it is often the case that hardware or software optimizations that take less time save energy overall even if the optimization takes a bit more energy when it is used. One reason is that all the rest of the computer is consuming energy while the program is running, so even if the optimized portion uses a little more energy, the reduced time can save the energy of the whole system.

- Pitfall: Using a subset of the performance equation as a performance metric.

	- nearly all proposed alternatives to the use of time as the performance metric have led eventually to misleading claims, distorted results, or incorrect interpretations.

	- MIPS (million instructions per second)

		> A measurement of program execution speed based on the number of millions of instructions. MIPS is computed as the instruction count divided by the product of the execution time and 10 ^ 6.

	- three problems with using MIPS as a measure for comparing computers

		1. MIPS specifies the instruction execution rate but does not take into account the capabilities of the instructions. We cannot compare computers with different instruction sets using MIPS, since the instruction counts will certainly differ

		2. MIPS varies between programs on the same computer; thus, a computer cannot have a single MIPS rating.

		3.  if a new program executes more instructions but each instruction is faster, MIPS can vary independently from performance!


**Questions **

a. Computer A has higher MIPS (4,000) compared to Computer B (3,636)

b. Comuter B is faster in terms of CPU time (35.2), compared to computer A (40)


