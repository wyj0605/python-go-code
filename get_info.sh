#!/bin/bash
#IP地址
function ip(){
    IP=`ifconfig | grep inet | grep -vE 'inet6|127.0.0.1' | awk -F ' ' '{print $2}'`
    echo $IP
}
#服务器型号
function xinghao () {
    P=`dmidecode|grep "Product"` 
    echo $P
}
#系统内存
function memory(){
    MEM=`cat /proc/meminfo|grep MemTotal|awk '{print $2}'`;   
    MEM_COUNT=`dmidecode -t memory|grep Size|grep -v 'No Module Installed'|wc -l`
    echo $MEM/1000/1000|bc;echo $MEM_COUNT

}
#操作系统版本
function os_version(){
    os_v=`cat /etc/redhat-release`
    echo $os_v
}
#操作系统位数
function os_weishu(){
    O_V=`uname -m`
    echo $O_V
}
#网卡信息
function net(){
    echo `ls /etc/sysconfig/network-scripts/ifcf*|grep -v 'ifcfg-lo'|wc -l`
    #echo `lspci | grep -i eth|wc -l`
}
#raid信息
function raid(){
   echo `lspci|grep RAID`
}
#磁盘使用情况 
function disk() {
    fs=$(df -h |awk '/^\/dev/{print $1}')
    for p in $fs; do
        mounted=$(df -h |awk '$1=="'$p'"{print $NF}')
        size=$(df -h |awk '$1=="'$p'"{print $2}')
        used=$(df -h |awk '$1=="'$p'"{print $3}')
        used_percent=$(df -h |awk '$1=="'$p'"{print $5}')
        echo "$mounted , 总大小: $size , 使用: $used , 使用率: $used_percent"
    done
}
function name () {
get_data="select (sum(bytes)/1024/1024/1024 ) || ' GB' from dba_data_files;"
get_dst="select subStr(file_name,1,instr(file_name,'.')-7) from dba_data_files where file_name like '%system%' and rownum<2;"
su - oracle -c "sqlplus -S / as sysdba <<eof
set heading off
${get_dst}
${get_data}
quit;

eof" >/tmp/revoke_user.txt 2>&1
    cat /tmp/revoke_user.txt|grep -v '^$'|tr '\n' '	'
}
ip
xinghao
memory
os_version
os_weishu
net
raid
disk
name


