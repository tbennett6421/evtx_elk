FROM sebp/elk

ENV NO_PROXY="localhost, 127.0.0.1/8,"
ENV SSL_CERT_FILE="/etc/ssl/certs/ca-certificates.crt"
ENV CURL_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt"
ENV REQUESTS_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt"
ENV AWS_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt"

# Copy enterprise ca's to ca-certificates locally

# Add to System CA trust
RUN update-ca-certificates -v -f

# Delete certs and supress failures
# Add certs to keystore

WORKDIR ${LOGSTASH_HOME}
RUN gosu logstash /opt/logstash/bin/logstash-plugin install logstash-filter-csv
RUN gosu logstash /opt/logstash/bin/logstash-plugin install logstash-codec-csv
