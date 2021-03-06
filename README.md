# Abnormal packets detection

The Fourth Industrial Revolution is focusing on Artificial Intelligence technologies to explore and mine data. Most devices are now connected through the Internet, so cybersecurity issues have raised concerns. This work has built network services in a virtual environment to experiment network attacks with various techniques. In such an environment, we have implemented Honeynet architecture to collect attack data for further research.  Our contributions include multi-folds. First, we deployed Honeynet architecture to collect data on actual cyber-attacks performed by real hackers and crackers. Also, we propose some techniques to normalize data and collect the HNET20 dataset with 29 extracted features including 200,000 samples experimented from 11 types of network attacks. Moreover, we design and propose the Adaptive Cybersecurity (AC) network system to detect attacks and provide warnings. The system reveals higher performance comparing to Snort method in detecting dangerous malicious attacks. Finally, we have experimented with different cyber-attacks to exploit the 10 Website security risks recommended by OWASP. From the research results, we can conclude that a typical cybercriminal attack cycle includes seven stages: reconnaissance, weapon making, distribution, exploitation, installation, control and control, and the goal. In this case, we proactively interrupt any action in the cybercriminal's attack cycle by early warnings using the Cyber Attack Warning and Detection System (AC) to prevent a potential cyber-attack.

# Dataset HNET20

  |      | Normal | Low | Medium | High|
  |------|--------|-----|--------|-----|
  | Sample | 78,564 | 12,346 | 107,086 | 990 |
  | Percent |39,48% | 6,20% | 53,82%| 0,50% |

  <p align="left">
  <img src="app/static/images/dataset.png"  alt="Dataset" width="40%"/>
  
  Figure 1. Percentage Distribution of HNNET20
  </p>
  
# Data visualization with LDA

  <p align="center">
  <img src="app/static/images/lda.png"  alt="Dataset" width="100%"/>
  Figure 2. Represent the collected data on the 2D graph
  </p>
  
# Experimental Results

  <p align="center">
  <img src="app/static/images/result.jpg"  alt="Dataset" width="100%"/>
  Figure 3. ACC and AUC results for the 2-class and 4-class classification problem
  </p>
  
# Installation

- Create and use environment variable
```
  python3 -m venv venv
  source venv/bin/activate
```
- Clone the repository and install the require packages
```
  git clone https://github.com/dzokha/ids-ac.git
  cd ids-ac
```
- Install the packages
```
  pip3 install -r requirements.txt
```
- Create table for Database
```
  flask db init
  flask db migrate
  flask db upgrade
```
- Run IDS-AC
```
  ./start.sh
```
# Visit Homepage

  http://localhost:8181/

  <p align="center">
  <img src="app/static/images/monitoring.png"  alt="Homepage" width="100%"/>
  Figure 4. Online network monitoring interface with IDS-AC
  </p>

