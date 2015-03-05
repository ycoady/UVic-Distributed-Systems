LAB #8 TASKS:
=============

PART 1 (WARM UP):
=================
1. Login to a westgrid cluster (see below PART 2).
2. Upload mpi_test.c, mpi_mmul.c and mpilab.pbs

mpicc -o mpitest mpitest.c
	
3. Compile mpi_test.c and run it using PBS (mpilab.pbs) on 4 nodes.


PART 2 (MATRIX MULTIPLICATION):
===============================
1. Let A, B, and C be square matrices of size NxN.
What is the running time in N of a NAIVE and SERIAL
implementation of the matrix multiplication algorithm
computing C = A*B? 
Is matrix multiplication a "nice" problem?
Can we do better than the naive implementation?

2. To familiarize yourself with matrix multiplication in C
compile mpi_mmul.c as non-MPI-program and then running the 
sanity_check() function: 

gcc mpi_mmul.c -o mpi_mmul
./mpi_mmul

3. Modify mpi_mmul.c to run as an MPI program that partitions, and distributes the work to multiply the matrices A and B among the number of nodes you specified when submitting your job to the PBS system.

4. Record the running time of your MPI program when setting the matrix size to NxN=4096x4096 and using the following number of MPI processes:
NPROC = {32, 16, 8, 4, 2, 1}

5. Calculate and plot the speedup as a function of used parallel MPI processes. Speedup is defined as:
 
(time req. for serial run)/(time req. for parallel run)
 


AVAILABLE WESTGRID SYSTEMS WITH MPI INSTALLED
=============================================
 UVIC:       hermes.westgrid.ca / nestor.westgrid.ca
 SFU:        bugaboo.westgrid.ca
 U. ALBERTA: jasper.westgrid.ca
 
 LOGIN:
 ssh username@hermes.westgrid.ca


USEFUL LINKS
============
 WESTGRID:
 https://www.westgrid.ca/support/systems/hermesnestor
 https://www.westgrid.ca/support/running_jobs

 PBS SCRIPTING:
 https://www.westgrid.ca/files/PBS%20Script_0.pdf
 
 MPI API DOCUMENTATION:
 http://www.mpich.org/static/docs/v3.1/

 API CALLS YOU WILL NEED:
  MPI_Init
  MPI_Comm_size
  MPI_Comm_rank
  MPI_Bcast
  MPI_Gather
  MPI_Finalize


GENERAL PROCEDURE OF RUNNING MPI PROGRAMS ON WESTGRID
=====================================================
1. Compile your MPI program:
	mpicc mpi_test.c -o mpi_test
		
3. Run a PBS script to submit a batch job to a westgrid cluster.
The preferred way of starting MPI programs on westgrid is mpiexec. The main advantage of using mpiexec over mpirun is that there is no need to source any setup files before executing your program. The example MPI program mpi_test.c could be executed with the PBS script contained with this lab as follows

	qsub -l procs=16,pmem=1gb,walltime=1:00:00 mpilab.pbs

in which 16 processors are requested (procs parameter), using at most 1 GB of memory per process (pmem parameter) and running for at most 1 hour (walltime parameter) (see https://www.westgrid.ca/support/running_jobs for more details).

4. Check your MPI program output:
The output files for the job are created in the same directory where the qsub command was executed. The output files are created using the same filename as your PBS script filename with an extension that includes "e" for "error" or "o" for "output" followed by the process number.