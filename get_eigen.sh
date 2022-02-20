#!/usr/bin/bash
set -e
git clone \
    --depth 1 \
    --filter=blob:none \
    --sparse \
    https://gitlab.com/libeigen/eigen.git \
;
cd eigen
git sparse-checkout set Eigen
cd ..
mv eigen eigen_
mv eigen_/Eigen .
rm -rf eigen_
echo "eigen downloaded successfully!"
