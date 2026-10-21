# Tech Stack Evaluation

## Project
Dynamic Micro-Learning Platform using ELO Rating and Bayesian Knowledge Tracing

## Requirements that drive the decision
- **FR2:** System shall match and deliver questions dynamically to students using Elo rating matchmaking algorithm based on student skill ratings and question difficulty ratings.
- **FR4:** System shall evaluate student concept mastery probability using Bayesian Knowledge Tracing (BKT) based on prior knowledge, learn rate, guess rate and slip rate.
- **FR6:** System shall log all student attempt interactions, response correctness and Elo/BKT parameter for model evaluation.
- **NFR1:** System shall recalculate Elo ratings and update the BKT mastery probability within 800 milliseconds of student answer submission.
- **NFR4:** User interface shall render question cards and interactive feedback responsively within 2 seconds across modern desktop and mobile web browsers.

## Options
- **Option A:** Static website (HTML, CSS, and vanilla JavaScript) hosted on GitHub Pages with browser localStorage (no backend database).
- **Option B:** Traditional Python web app (Flask + local SQLite database) hosted on a basic cloud server (single web interface for both students and teachers).
- **Option C:** React Native (Expo) for student's mobile app + React/Next.js for teachers/admin web dashboard + Supabase for database , Auth and backend .

## Decision matrix
Weight: how important the criterion is for YOUR project (1 = low, 5 = high).
Score: how well each option does (1 = poor, 5 = excellent).

| Criterion                          | Weight | A score | B score | C score |
|------------------------------------|--------|---------|---------|---------|
| Fits my requirements               | 5      | 1 (5)   | 3 (15)  | 5 (25)  |
| Skills I already have              | 4      | 4 (16)  | 3 (12)  | 4 (16)  |
| Time to build before my deadline   | 4      | 5 (20)  | 4 (16)  | 4 (16)  |
| Free hosting and tools             | 4      | 5 (20)  | 3 (12)  | 5 (20)  |
| Performance and security needs     | 5      | 2 (10)  | 4 (20)  | 5 (25)  |
| Room to grow later                 | 3      | 1 (3)   | 3 (9)   | 5 (15)  |
| **Total (weighted)**               |        | **74**  | **84**  | **117** |

## Decision record
- **Context:** My project serves two user roles: Students doing microlearning quizzes (mobile app) and educator managing the question bank while monitoring live analytics (web app). 

- **Decision:** **Option C** — React Native (Expo) for the student mobile app + React/Next.js web dashboard for teachers + Supabase(PostgreSQL) for unified backend.

- **Reasons:**
  1. Fits functional and non functional requirements: Both student Expo app and the teacher web portal connect to the same Supabase PostgreSQL database. When students answer questions on mobile, the Elo and BKT math executes in milliseconds and logs every parameter for model evaluation.
  2. Solves the issue of live FYP demonstration : Supabase broadcasts database changes instantly. So educators watching the web dashboard can view student-question matchmakings and mastery bars recalibrate live as students answers on the Expo mobile app.

- **Consequences:**
  - *What becomes easy:* Testing mobile app prototype immediately on a real phone via Expo Go while sharing TypeScript code and Supabase queries between mobile and web enable live rating updates during final presentation.
  - *What becomes harder:* Maintaining two separate frontend interfaces (student mobile app on Expo + web dashboard for educators) adds more UI work.

- **Risks and next review:** Building both a mobile app and a web admin portal could cause UI scope clash in case of over-design. So I can prevent this by keeping the teacher web dashboard focused strictly on question entry and the Elo/BKT analytics table. *If maintaining both Expo mobile and React web takes too much time* , I can always compile the Expo app directly to the web or use a single responsive Next.js web app while relying on the exact same Supabase backend.