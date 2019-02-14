from timeit import default_timer
from math   import gcd

# ===========================================================
# FUNCTION: generate_pythagorean_triples
# ===========================================================
#
# INPUT:    integer representing the maximum possible perimeter
#           of the pythagorean triple triangle
#
# OUTPUT:   List containing length-3 lists (list of each Pythagorean
#           triple whose perimeter is less than the input)
#
# TASK:     using the quadratic equation approach to
#           generating Pythagorean triples to compute all
#           triples whose perimeter is <= the input parameter
#
# ALGORITHM:
#   1.  Pythagorean triples are sets of 3 integers (a,b,c), which
#       satisfy the condition a^2 + b^2 = c^2
#   2.  The Quadratic approach states the following to be true:
#           m+n is an odd number
#           m>n
#           m and n are relatively prime (gcd of m,n is 1)
#           if the above conditions hold true, then:
#               a = m^2 - n^2
#               b = 2mn
#               c = m^2 + n^2
#               and a Pythagorean triple (d*a, d*b, d*c)
#               exists for all positive integers d
#
# NOTES:
#   This formula was derived from:
#       https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
#
#   The specific algorithm used employs the "Generating Triples
#   Using Quadratic Equations" method
#
# ===========================================================
def generate_pythagorean_triples( max_perimeter ):
    # Prepare Variables
    triples  =  [ ]
    m        =  2
    n        =  1

    # Outer loop continues for as long as C (m^2+n^2) is < max perimeter
    # A tighter bound is possible, but this is sufficient
    while ( ( m * m ) + ( n * n ) ) <= max_perimeter:
        # We only consider n<m so that we do not repeat triples (a,b,c) and (b,a,c)
        while n < m:
            # If m and n are co-prime their sum is odd
            if ( ( ( m + n ) % 2 ) == 1 ) and ( gcd( m , n ) == 1 ):
                a  =  ( m * m ) - ( n * n )
                b  =  2 * m * n
                c  =  ( m * m ) + ( n * n )

                # No point in considering the triple if its perimeter is
                # larger than the masimum limit parameter
                if ( a + b + c ) <= max_perimeter:
                    # Determine all d such that the perimeter fits the constraints
                    d  =  1
                    while d * ( a + b + c ) <= max_perimeter:
                        triples.append( [ d * a , d * b , d * c ] )
                        d  +=  1

                # If perimeter is too large, all future m,n pairs will also generate
                # perimeters too large -- safe to break while n<m loop
                else:
                    break

            # Increment n (while n<m)
            n  +=  1
        # Increment m and reset n to 1 (while m*m+n*n< maximum_perimeter)
        m  +=  1
        n   =  1

    # Return list containing all pythagorean triples that fit the constraint
    return triples



# ===========================================================
# PROBLEM 9 -- Special Pythagorean triplet
# ===========================================================
#
# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which
#       a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#
# There exists exactly one pythagorean triplet for which
# a + b + c = 1000.
#
# Find the product a*b*c
#
# ===========================================================
def problem_9( ):
    # Print Problem Context
    print( "Project Euler Problem 9 -- Special Pythagorean Triples" )

    # Set Up Variables
    start_time  =  default_timer( )
    triples     =  generate_pythagorean_triples( 1000 )
    result      =  1

    # Primary Loop -- iterate over to determine which perimeter equals 1000
    for triangle in triples:
        # Result is Found (perimeter = 1000)
        if sum( triangle ) == 1000:
            # Compute product of the sides
            for side in triangle:
                result  *=  side
            break  # Only expected result found, break loop
        continue  # added for readability

    # Compute Execution Time
    end_time        =  default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000
    print( "   a*b*c of Pythagorean Triple whose sum is 1000:   %d"      %  result )
    print( "   Computation Time:                                %.3fms"  %  execution_time )
    return



if __name__ == '__main__':
    problem_9( )