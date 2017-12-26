#!/bin/bash
echo "Running Python2.7 tests"
echo "========================"
echo ""
python2.7 -m unittest tests
echo ""
echo ""
echo "Running Python3 tests"
echo "========================"
echo ""
python3 -m unittest tests