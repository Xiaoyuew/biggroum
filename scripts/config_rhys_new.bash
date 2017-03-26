#!/bin/bash

FIXR_GRAPH_EXTRACTOR=/home/ubuntu/FixrGraphExtractor
FIXR_GRAPH_INDEXER=/home/ubuntu/FixrGraphIndexer
FIXR_GRAPH_ISO_BIN=/home/ubuntu/FixrGraphIso/graph_build/src/fixrgraphiso/fixrgraphiso
FIXR_COMMUNITY_DETECTION=/home/ubuntu/FixrCommunityDetection
SPARK_SUBMIT_PATH=/home/ubuntu/spark-2.0.0-bin-hadoop2.7/bin/spark-submit

OUT_DIR=/home/ubuntu/graph_extraction_rhys_thesis

# Index options
MIN_METHODS=0
MIN_NODES=0
MIN_EDGES=0
MIN_COMMON_METHODS=0
MIN_WEIGHT=1

# ISO OPTIONS
TIMEOUT=5
JOB_SIZE=5000
