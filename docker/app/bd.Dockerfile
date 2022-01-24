FROM postgres:13
ENV TERM=xterm
RUN apt-get update
RUN apt-get install -y nano iptables