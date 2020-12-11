#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import requests
import json
import org.slf4j.LoggerFactory as LoggerFactory

logger = LoggerFactory.getLogger("Xray")


def getReports(serverParams, reportID, impactedArtifact):
    # Define api endpoint
    api_endpoint = '/api/v1/reports/vulnerabilities/%s?direction=asc&page_num=1&num_of_rows=10000' % reportID
    url = "%s%s" % (serverParams.get("base_url"), api_endpoint)

    # Setting up headers.
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % serverParams.get("token")
    }

    # Setting up payload.
    payload = json.dumps({
        "filters": {
            "impacted_artifact": impactedArtifact
        }
    })

    # API call
    r = requests.post(url, data=payload, headers=headers, verify=False)
    if r.status_code != 200:
        raise Exception(
            "Error connecting. Status Code: %s. Reason: %s" % (r.status_code, r.reason)
        )
    else:
        # Got a 200 response code, process response data.
        report = json.loads(r.content)
        cves = report['total_rows']

        sumCVSS2 = 0
        sumCVSS3 = 0
        numHigh = 0
        numMedium = 0
        numLow = 0

        for cve in report['rows']:
            if 'cvss2_max_score' in cve:
                sumCVSS2 += cve['cvss2_max_score']
            if 'cvss3_max_score' in cve:
                sumCVSS3 += cve['cvss3_max_score']
            if 'severity' in cve and cve['severity'] != 'Unknown':
                if cve['severity'] == 'High':
                    numHigh += 1
                elif cve['severity'] == 'Medium':
                    numMedium += 1
                else:
                    numLow += 1

        averageCVSS2Score = str(round(1.0 * sumCVSS2 / cves, 2)) if cves > 0 else "No Score"
        averageCVSS3Score = str(round(1.0 * sumCVSS3 / cves, 2)) if cves > 0 else "No Score"
        highSeverity = numHigh
        mediumSeverity = numMedium
        lowSeverity = numLow
        output = report

        return cves, highSeverity, mediumSeverity, lowSeverity, averageCVSS2Score, averageCVSS3Score, output
