echo "Part 1"
grep -Er "^(AB)+(CB)+(CD)+(ED)+(EF)+(AF)+(AB)+(AB|AF|CB|CD|ED|EF){0,3}$" ../../docs/obtuse_new
echo "Part 2"
grep -Er "^(AB)+(AF)+(EF)+(ED)+(CD)+(CB)+(CB)+(AB|AF|CB|CD|ED|EF){0,3}$" ../../docs/obtuse_new