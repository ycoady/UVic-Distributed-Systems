/* #include <mpi.h> */
#include <stdio.h>
#include <unistd.h>

const int size = 3;
/* const int size = 4096; */

float a[size][size];
float b[size][size];
float c[size][size];

/* Print matrix values to console */
void print_matrix(float matrix[size][size])
{
	int i, j;
	for (i = 0; i < size; ++i)
	{
    	for(j = 0; j < size; j++)
		{
        	printf("%6.2f\t", matrix[i][j]);
		}
    	printf("\n");
	}
}
 
/* Initialize matrices */
void init_matrices()
{
	int i, j;
	// Initialize matrices.
	for (i = 0; i < size; ++i)
	{
		for (j = 0; j < size; ++j)
		{
        	a[i][j] = (float)i + j;
            b[i][j] = (float)i - j;
            c[i][j] = 0.0f;
         }
	 }
}

/* Multiply specified sections of the matrices */ 
void multiply(int idx_start, int idx_end)
{
	int i, j, k;
	for (i = idx_start; i <= idx_end; ++i)
	{
		for (j = 0; j < size; ++j) 
		{
			for (k = 0; k < size; ++k) 
			{
            	c[i][j] += a[i][k] * b[k][j];
			}
		}
	}
}
 
/* Print values of matrices A, B, and C = A*B */ 
void sanity_check()
{
	printf("A:\n");
	print_matrix(a);
	printf("\n");
	
	printf("B:\n");
	print_matrix(b);
	printf("\n");
	
	multiply(0, size-1);
	printf("C = A*B:\n");
	print_matrix(c);
}

int main(int argc, char **argv)
{
    int rank, nproc;
    int idx_start, idx_end;
	
	/* TODO: Initialize MPI subsystem 
	   will need MPI_COMM_WORLD as parameter what does it do?*/
	
	/* TODO: deterimine (1) total number of MPI nodes (nproc) and
	   (2) the nodes own MPI rank (rank)*/
	
	/* TODO: populate matices with some values 
   	   (Modify this such that only MPI node with rank 0 
	   is calling this routine!) */
	init_matrices();
	
	/* TODO: have rank 0 node BROADCAST values of 
	   matrix A, B, C to all MPI workers (workers have rank 1..(procs-1) )
	   (datatype: MPI_FLOAT, you may also use MPI_Scatter instead of broadcasting) */
	
	/* TODO: partition work, that is:
		idx_start = (size / procs) * rank;
	    idx_end = ? */
	
	/* TODO: Compute matrix multiplication in assigned
	   partition [idx_start, idx_end] */
	
	/* TODO: Gather computed results */
		
	/* Print matrices (sanity check, only run for small matrix size) 
	   (TODO: comment this line out when running as MPI program).*/
	sanity_check();
}