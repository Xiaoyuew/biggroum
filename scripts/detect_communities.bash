#!/bin/bash

check_exists(){
    local file=$1
    local msg=$2

    if [ ! -f "${file}" ] && [ ! -d "${file}" ] ; then
        echo "${msg}: ${file} does not exists!"
        exit 1
    fi
}


check_res() {
    local res=$1
    local msg=$2

    if [ "${res}X" != "0X" ]; then
        echo "Error code ${res}: ${msg}"
        exit 1
    fi
}


rl="$(readlink -f "$0")"
script_dir="$(dirname "${rl}")"

config_script=$1

#config_script="${script_dir}/config.bash"

check_exists "${config_script}" "config.bash script was not provided!"

source ${config_script}

FIXR_GRAPH_EXTRACTOR_JAR="$(readlink -f ${FIXR_GRAPH_EXTRACTOR}/target/scala-2.11/fixrgraphextractor_2.11-0.1-SNAPSHOT-one-jar.jar)"
FIXR_COMMUNITY_DETECTION_JAR="$(readlink -f ${FIXR_COMMUNITY_DETECTION}/target/scala-2.11/FixrCommunityDetection-assembly-0.1-SNAPSHOT.jar)"

check_exists "${FIXR_GRAPH_EXTRACTOR}" "FixrGraphExtractor folder"
check_exists "${FIXR_GRAPH_EXTRACTOR_JAR}" "FixrGraphExtractor jar does not exist: did you run sbt oneJar there?"
check_exists "${FIXR_GRAPH_INDEXER}" "FixrGraphIndexer folder"
check_exists "${FIXR_GRAPH_ISO_BIN}" "FixrGraphIso binary"
check_exists "${FIXR_COMMUNITY_DETECTION}" "FixrCommunityDetection path"
check_exists "${FIXR_COMMUNITY_DETECTION_JAR}" "FixrCommunityDetection jar does not exist: did you run sbt assembly there?"
check_exists "${REPO_LIST}" "List of repositories"
check_exists "${SPARK_SUBMIT_PATH}" "Spark submit executable"

FIXR_GRAPH_PYTHON="$(readlink -f "${script_dir}/../python/fixrgraph/")"
check_exists "${FIXR_GRAPH_PYTHON}" "Python package"

if [ -d "${OUT_DIR}" ] ; then
    echo "${OUT_DIR} already exists. Continuing anyways..."
fi
mkdir -p "${OUT_DIR}"

OUT_LOG=${OUT_DIR}/out_log_community.txt

echo "Running community detection..."
# Generate the list of isomorphisms
##########################################################################################################################################################
# echo "Extracting isomorphism..."															 #
# echo "python ${FIXR_GRAPH_PYTHON}/db/scripts/filter_isos.py -d ${OUT_DIR}/graphs_db.db -o ${OUT_DIR}/iso_list.txt -w 10 &>> ${OUT_LOG}" &>> ${OUT_LOG} #
# python ${FIXR_GRAPH_PYTHON}/db/scripts/filter_isos.py -d ${OUT_DIR}/graphs_db.db -o ${OUT_DIR}/iso_list.txt -w 10 &>> ${OUT_LOG}			 #
# check_res "$?" "Extracting isomorphism"														 #
##########################################################################################################################################################

# Run the community detection
echo "Computing communities..."
echo "${SPARK_SUBMIT_PATH} --class edu.colorado.plv.fixr.community.Main ${FIXR_COMMUNITY_DETECTION_JAR} -w iso -i ${OUT_DIR}/iso -f ${OUT_DIR}/iso_list.txt -o ${OUT_DIR}/communities"
${SPARK_SUBMIT_PATH} --class edu.colorado.plv.fixr.community.Main ${FIXR_COMMUNITY_DETECTION_JAR} -w iso -i ${OUT_DIR}/iso -f ${OUT_DIR}/iso_list.txt -o ${OUT_DIR}/communities &>> ${OUT_LOG}
check_res "$?" "Community detection"

