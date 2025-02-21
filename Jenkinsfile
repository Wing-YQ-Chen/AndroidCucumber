pipeline {
	agent any
    stages {

		stage('Setup testing environment') {
			steps {
				bat """
				echo "Dolwnload App"
                echo "Install App by adb"
                """
            }
        }

        stage('Build Testing') {
			steps {
				bat """
				echo "Build"
                python -m venv venv
                call venv\\Scripts\\activate。
                pip list
                pip install -r requirements.txt -i "https://mirrors.aliyun.com/pypi/simple/"
                pip list
                """
            }
        }


		stage('Run Testing') {
			steps {
				bat """
				echo "Run Testing"
				python features\\steps\\Tb_Coupon_Query.py
				"""
			}
			post {
				always {
					archiveArtifacts artifacts: 'Execution\\**', allowEmptyArchive: true
				}
			}
		}
		
    }
}