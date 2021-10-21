FROM sebp/elk

ENV HTTP_PROXY="http://proxy.example.com:8080"
ENV HTTPS_PROXY="http://proxy.example.com:8080"
ENV NO_PROXY="localhost, 127.0.0.1/8,"
ENV SSL_CERT_FILE="/etc/ssl/certs/ca-certificates.crt"
ENV CURL_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt"
ENV REQUESTS_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt"
ENV AWS_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt"

# Copy enterprise ca's to ca-certificates locally
COPY ./certs/example-policy.crt /usr/local/share/ca-certificates/example-policy.crt
COPY ./certs/example-root.crt /usr/local/share/ca-certificates/example-root.crt
COPY ./certs/example-enterprise-issuing.crt /usr/local/share/ca-certificates/example-enterprise-issuing.crt

# Add to System CA trust
RUN update-ca-certificates -v -f

# Delete certs and supress failures
RUN keytool -delete -alias ex_root_cert -keystore /opt/logstash/jdk/lib/security/cacerts -storepass changeit > /dev/null 2>&1 || return 0
RUN keytool -delete -alias ex_pol_cert -keystore /opt/logstash/jdk/lib/security/cacerts -storepass changeit > /dev/null 2>&1 || return 0
RUN keytool -delete -alias ex_ei_cert -keystore /opt/logstash/jdk/lib/security/cacerts -storepass changeit > /dev/null 2>&1 || return 0
# Add certs to keystore
RUN keytool -import -trustcacerts -keystore /opt/logstash/jdk/lib/security/cacerts -storepass changeit -noprompt -alias ex_root_cert -file /usr/local/share/ca-certificates/example-root.crt
RUN keytool -import -trustcacerts -keystore /opt/logstash/jdk/lib/security/cacerts -storepass changeit -noprompt -alias ex_pol_cert -file /usr/local/share/ca-certificates/example-policy.crt
RUN keytool -import -trustcacerts -keystore /opt/logstash/jdk/lib/security/cacerts -storepass changeit -noprompt -alias ex_ei_cert -file /usr/local/share/ca-certificates/example-enterprise-issuing.crt

WORKDIR ${LOGSTASH_HOME}
RUN gosu logstash /opt/logstash/bin/logstash-plugin install logstash-filter-csv
RUN gosu logstash /opt/logstash/bin/logstash-plugin install logstash-codec-csv
