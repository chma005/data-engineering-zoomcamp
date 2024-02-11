<!-- Video 1 -->
orchestration is key to data tanformation. Every work flow requires sequential steps.
Steps = tasks
Extract, tranform, and load.
Orchestration is key to building workflows.
<!-- Video 2 Intro to mage-->
Mage was built to build data workflows. 
Mage is an open source pipeline 
Projects form the basis for all the work in Mage
Pipelines: perform some operation
Blocks: files that can executed in a pipeline.
Anatomy of a block:
first imports, then decorator: 
function that returns a data frame
test or insertion: ran on outpur df.
This if very similar to my routes in batch app project.

Running docker pull mageai/mageai:latest will bring in the latest mage

It's always a good idea to put passwords in .env fies then accessing these varialbe via code blocks like
$(NAME)

In mage, you interact with files with jinja syntax! {{}}

When loading data into mage via csv file, it is a best practice to map data types