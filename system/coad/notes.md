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


