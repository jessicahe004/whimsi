# immerse yourself in new worlds (work in progress)
Whimsi is an web application that allows users to visualize their reading journey by uploading a pdf file (a story) and receive a series of chronological scenes corresponding to page numbers. 

# inspiration! 
I took a course: 'Comparative Culture Teaching in Today’s Society: Careers in Special Education' where I learned about intentional steps taken towards creating inclusive classrom. 

(sketch-notes for the course) 

<img width="393" alt="Screenshot 2024-08-05 at 1 24 23 AM" src="https://github.com/user-attachments/assets/9f39834a-ed1f-4806-a003-5d1f637d3464">


Specifically, I wanted to explore the picture exchange communication system (PECS), which is an augmentative and alternative communication (AAC) system that utilizes pictures to enable individuals with communication difficulties to express their needs and desires in a non-verbal manner. 

Before beginning my project, I reached out to my professor for additional research to which she linked two papers on reading comprehesion: https://ila.onlinelibrary.wiley.com/doi/full/10.1002/rrq.411 and https://www.literacyworldwide.org/docs/default-source/bonus-materials/front-matter-710.pdf. 

For my project, I aimed to make general reading materials more engaging and comprehensive. Once I tackled this, I want to explore conjunctions, prepositions, and more abstract terms. 

Problem Statement - Elementary students (6-10) can struggle to transition from picture books to chapter books because of inexperienced fluency, matured content, lack of feedback, and shortened attention span. 

# solution - turn every chapter book into a picture book 
- Start storyboards for your favorite chapter book to track reading progress.
- Machine learning for scanning by page number, chunking to maintain in-order setence structure, and removing filler words for prompting.
- Environmental scenes generated for each upload check-point. 

# meet the tools 
- React.js frontend for a simple interface.
- Third.js for adding animation on landing-page. 
- FastAPI backend for building quick micro-services. 
- PyMuPDF for scanning and extracting text from PDF file to return a list of chunks.
- TBD model for fine-tuning and filtering the list of chunks into appropriate prompts.
- TBD image generator run on a local server for image generation.

# learning process - "premature optimization is the root of all evil"
(i will link my system design drafts)

MVP
- check-point #1: landing page, upload file -> text extracted https://www.capcut.com/s/CVzWZkWEvW5qPJA1/
- checkpoint #2: prompt generation 
- checkpoint #3: image generation

NEXT STAGE
- check-point #1: tokenization (exploring sliding window tokens, variable tokens) 
- check-point #2: semantic search
- check-point #3: optimize processing time 

# next steps for whimsi
- Implement a RAG pipeline to create consistent visuals when adding more elements i.e humans, animals.
- Experiment with user preferences for processing time and different chunking techniques i.e uploading entire book versus chapter by chapter. 

# closing notes
I hope this application speaks to families, but most importantly towards your inner child that thought reading was boring because you weren't able to immerse yourself in a book.  
