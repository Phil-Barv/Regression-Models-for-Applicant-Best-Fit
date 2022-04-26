# Applicant Best-Fit

<br>

This project uses linear regression models to create plots that show an applicants 
best-fit to an organization based on the quality of their scores on prompts with
increasing difficulty. Details to run the app locally are provided below.

- Y-axis: Quality of Explanation
- X-axis: Difficulty of the Task

<br>

## Example Behavioral Prompts (With Increasing Difficulty)

<blockquote>
    <b>Prompt 1:</b> What's your quirky feature?
    <br><br>
    <b>Prompt 2:</b> If you were to meet a person in a similar position, what would you ask them?
    <br><br>
    <b>Prompt 3:</b> What are some ways you can leverage your network to bring in partner companies to recruit students for opportunities?
    <br><br>
    <b>Prompt 4:</b> How would you handle a student exhibiting frustration with their hiring experience?
    <br><br>
    <b>Prompt 5:</b> How would you handle competing deadlines?
    <br><br>
    <b>Prompt 6:</b> How do you write a cover letter/ resume?
    <br><br>
    <b>Prompt 7:</b> If you are working on a team project and a colleague suggests a strategy that you feel strongly will take the project in a bad direction. What do you do?
    <br><br>
    <b>Prompt 8:</b> What would you do if a team member refuses to, or just can not complete their part of the work? Give an example.
    <br><br>
    <b>Prompt 9:</b> How would you handle communication with a recruiting team of a company after a student of yours has had their offer unexpectedly rescinded? 
    <br><br>
    <b>Prompt 10:</b> If you were to start today, what is the first change you would implement?
</blockquote>

<br>

From the prompts above, we can assume that we had three candidates Missy, Stacie, and Sussie, whose performances followed log, uniform,
and exponential distribution respectively.

### Log Distribution

```python
applicantLogPerformance = fitting(difficulty, applicantLog, 'Missy', scale=10)
```

<br>

<p align="center">
  <img src="plot/missy.png" alt="Applicant Log Performance"/>
</p>

<br>

### Exponential Distribution

```python
applicantExponPerformance = fitting(difficulty, applicantExpon,'Susie', scale=20)
```

<br>

<p align="center">
  <img src="plot/susie.png" alt="Applicant Exponential Performance"/>
</p>

<br>

### Uniform Distribution

```python
applicantUniformPerformance = fitting(difficulty, applicantUniform, 'Stacie', scale=50)
```

<br>

<p align="center">
  <img src="plot/stacie.png" alt="Applicant Uniform Performance"/>
</p>

<br>

## Running the application locally

1. Clone the repo to your local machine!
2. Open your terminal and cd to the location of the cloned repo.
3. In the clone's root directory, input:

#### macOS
```python3
python3.6 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3.6 example.py
```

#### Windows
```python3
python3.6 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3.6 example.py
```

#### Git Bash
```python3
python3.6 -m venv venv
venv/Scripts/activate.bat
pip3 install -r requirements.txt
python3.6 example.py
```

4. Once you run the commands, the app will generate the figures for the three example applicants and store them in the plots directory.
5. Feel free to adapt the code to your dataset.