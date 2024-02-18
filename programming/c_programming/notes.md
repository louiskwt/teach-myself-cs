# C Programming Notes

**The spirit of C**

- Trust the programmer. Generally speaking, the C language assumes you know what you’re doing and lets you. This isn’t always a good thing (for example, if you don’t know what you’re doing).

- Don’t prevent the programmer from doing what needs to be done. Because C is a system programming language, it has to be able to handle a variety of low-level tasks.

- Keep the language small and simple. The language is designed to be fairly close to the hardware and to have a small footprint.

- Provide only one way to do an operation. Also known as conservation of mechanism, the C language tries to limit the introduction of duplicate mechanisms.

- Make it fast, even if it isn’t guaranteed to be portable. Allowing you to write optimally efficient code is the top priority. The responsibility of ensuring that code is portable, safe, and secure is delegated to you, the programmer.

The C programming language was developed in 1972 by Dennis Ritchie and Ken Thompson at Bell Telephone Laboratories

**The C Standard**

- In 1990, the ANSI C Standard was adopted (unchanged) by a joint technical committee of the International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC) and published as the first edition of the C Standard, C90 (ISO/IEC 9899:1990). The second edition of the C Standard, C99, was published in 1999 (ISO/IEC 9899:1999), and a third edition, C11, in 2011 (ISO/IEC 9899:2011). The latest version of the C Standard (as of this writing) is the fourth version, published in 2018 as C17 (ISO/IEC 9899:2018). A new major revision referred to as C2x is under development by ISO/IEC.

- As of 2024, C23 is the informal name for what will likely become ISO/IEC 9899:2024, the next standard for the C programming language, which will replace C17 (standard ISO/IEC 9899:2018). It was started in 2016 informally as C2x, and expected to be published in 2024.

- The C Standard (ISO/IEC 9899:2018) defines the language and is the final authority on language behavior.

The C Standard provides a substantial degree of latitude to implementations to allow them to be optimally efficient on various hardware platforms. Implementations is the term used by the C Standard to refer to compilers and is defined as follows:

> A particular set of software, running in a particular translation environment under particular control options, that performs translation of programs for, and supports execution of functions in, a particular execution environment.

**Implications of C Standard**

- each compiler with a particular set of command line flags, along with the C Standard Library, is considered a separate implementation, and different implementations can have significantly different implementation-defined behavior. This is noticeable in GNU Compiler Collection (GCC), which uses the -std= flag to determine the language standard. Possible values for this option include c89, c90, c99, c11, c17, c18, and c2x. The default depends on the version of the compiler. If no C language dialect options are given, the default for GCC 10 is -std=gnu17, which provides extensions to the C language. For portability, specify the standard you’re using. For access to new language features, specify a recent standard. A good choice (in 2019) with GCC 8 and later is -std=c17.

- Because of that, c program can behave differently based on the standard used during compilation
