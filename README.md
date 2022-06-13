# backup_restore_solver

As the task does not say explicitly that we obligated to use a Postgres database and restore it from the dump indeed,
I assumed that the easier way would suffice.
Therefore, my solution simply gets the encoded string from the site (using the provided access token), decodes and de-gzipes it.
Then we use regexp match to get all lines with SSN and `alive` at the end.

I fully understand that it might be not optimal and not efficient, and probably it might fail if input changes its format, but it solves the task on current set of inputs... 
