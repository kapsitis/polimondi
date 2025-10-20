#!/bin/bash

NN=30

python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABABAB.txt > ABABAB.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABABAF.txt > ABABAF.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABABCB.txt > ABABCB.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABABCD.txt > ABABCD.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABAFAB.txt > ABAFAB.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABAFAF.txt > ABAFAF.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABAFED.txt > ABAFED.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABAFEF.txt > ABAFEF.txt &

python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABCBAB.txt > ABCBAB.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABCBAF.txt > ABCBAF.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABCBCB.txt > ABCBCB.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABCBCD.txt > ABCBCD.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABCDCB.txt > ABCDCB.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABCDCD.txt > ABCDCD.txt &
python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABCDED.txt > ABCDED.txt &
# python poly_lists_metrics.py ../../docs/obtuse/obtuse_${NN}_ABCDEF.txt > ABCDEF.txt &
wait