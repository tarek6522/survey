document.addEventListener('DOMContentLoaded', () => {
    // 1. Smooth Scrolling for Navigation Links
    document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId && targetId !== '#') {
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // 2. Auth Page - Login/Signup Tab Switching & Validation
    const loginTab = document.getElementById('login-tab');
    const signupTab = document.getElementById('signup-tab');
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');

    if (loginTab && signupTab && loginForm && signupForm) {
        const switchAuthTab = (activeTab, inactiveTab, activeForm, inactiveForm) => {
            activeTab.classList.add('active');
            inactiveTab.classList.remove('active');
            activeForm.classList.remove('hidden');
            inactiveForm.classList.add('hidden');
        };

        switchAuthTab(loginTab, signupTab, loginForm, signupForm);

        loginTab.addEventListener('click', () => {
            switchAuthTab(loginTab, signupTab, loginForm, signupForm);
        });

        signupTab.addEventListener('click', () => {
            switchAuthTab(signupTab, loginTab, signupForm, loginForm);
        });

        loginForm.addEventListener('submit', (e) => {
            if (!loginForm.checkValidity()) {
                e.preventDefault();
                return;
            }
        });

        signupForm.addEventListener('submit', (e) => {
            if (!signupForm.checkValidity()) {
                e.preventDefault();
                return;
            }

            const password = document.getElementById('signup-password').value;
            const confirmPassword = document.getElementById('signup-confirm-password').value;

            if (password.length < 6) {
                e.preventDefault();
                alert('كلمة المرور يجب أن لا تقل عن 6 أحرف.');
                document.getElementById('signup-password').focus();
                return;
            }

            if (password !== confirmPassword) {
                e.preventDefault();
                alert('كلمتا المرور غير متطابقتين. يرجى التأكد.');
                document.getElementById('signup-confirm-password').focus();
                return;
            }
        });
    }

    // 3. Single Survey Page Logic (Progress Bar, Modal, etc.)
    const surveyForm = document.getElementById('surveyForm');
    const questions = document.querySelectorAll('.form-question');
    const prevBtn = document.getElementById('prev-question-btn');
    const nextBtn = document.getElementById('next-question-btn');
    const submitBtn = document.getElementById('submit-survey-btn');
    const progressBar = document.getElementById('survey-progress-bar');
    const progressText = document.getElementById('progress-text');

    const successModal = document.getElementById('successModal');
    const closeButton = successModal ? successModal.querySelector('.close-button') : null;
    const modalPointsSpan = successModal ? successModal.querySelector('.modal-content p span') : null;

    let currentQuestionIndex = 0;
    const totalQuestions = questions.length;
    const surveyPoints = 700;

    if (surveyForm && totalQuestions > 0) {
        const updateProgressBar = () => {
            const progress = ((currentQuestionIndex + 1) / totalQuestions) * 100;
            progressBar.style.width = `${progress}%`;
            progressText.textContent = `${Math.round(progress)}% مكتمل`;
        };

        const showQuestion = (index) => {
            questions.forEach((q, i) => {
                if (i === index) {
                    q.classList.add('current-question');
                    q.classList.remove('hidden');
                } else {
                    q.classList.remove('current-question');
                    q.classList.add('hidden');
                }
            });

            prevBtn.style.display = (index === 0) ? 'none' : 'inline-block';
            nextBtn.style.display = (index === totalQuestions - 1) ? 'none' : 'inline-block';
            submitBtn.style.display = (index === totalQuestions - 1) ? 'inline-block' : 'none';

            updateProgressBar();
        };

        showQuestion(currentQuestionIndex);

        nextBtn.addEventListener('click', () => {
            const currentInputs = questions[currentQuestionIndex].querySelectorAll('input[required], textarea[required]');
            let isValid = true;
            currentInputs.forEach(input => {
                if (!input.checkValidity()) {
                    isValid = false;
                    input.reportValidity();
                }
            });

            if (isValid && currentQuestionIndex < totalQuestions - 1) {
                currentQuestionIndex++;
                showQuestion(currentQuestionIndex);
            }
        });

        prevBtn.addEventListener('click', () => {
            if (currentQuestionIndex > 0) {
                currentQuestionIndex--;
                showQuestion(currentQuestionIndex);
            }
        });

        surveyForm.addEventListener('submit', (e) => {
            // Let the form submit normally
        });

        if (closeButton) {
            closeButton.addEventListener('click', () => {
                successModal.classList.add('hidden');
                successModal.classList.remove('visible');
            });
        }

        if (successModal) {
            successModal.addEventListener('click', (e) => {
                if (e.target === successModal) {
                    successModal.classList.add('hidden');
                    successModal.classList.remove('visible');
                }
            });
        }

        const q1Radios = document.querySelectorAll('input[name="q1"]');
        const q1OtherTextarea = document.querySelector('textarea[name="q1_other"]');

        if (q1Radios.length > 0 && q1OtherTextarea) {
            q1Radios.forEach(radio => {
                radio.addEventListener('change', () => {
                    if (radio.value === 'مصادر أخرى') {
                        q1OtherTextarea.classList.remove('hidden');
                        q1OtherTextarea.setAttribute('required', 'true');
                    } else {
                        q1OtherTextarea.classList.add('hidden');
                        q1OtherTextarea.removeAttribute('required');
                    }
                });
            });

            const selectedRadio = document.querySelector('input[name="q1"]:checked');
            if (selectedRadio && selectedRadio.value === 'مصادر أخرى') {
                q1OtherTextarea.classList.remove('hidden');
                q1OtherTextarea.setAttribute('required', 'true');
            } else {
                q1OtherTextarea.classList.add('hidden');
                q1OtherTextarea.removeAttribute('required');
            }
        }
    }

    // 4. Hero Section - Dynamic Background Image
    const heroSection = document.querySelector('.hero');
    const backgroundImages = [
        'https://images.unsplash.com/photo-1596568165034-7a134a6d714b',
        'https://images.unsplash.com/photo-1551608460-6dd831c2bbd3',
        'https://images.unsplash.com/photo-1579730538749-d3e2300b9795'
    ];
    let currentImageIndex = 0;

    if (heroSection && backgroundImages.length > 0) {
        heroSection.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('${backgroundImages[currentImageIndex]}')`;

        setInterval(() => {
            currentImageIndex = (currentImageIndex + 1) % backgroundImages.length;
            heroSection.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('${backgroundImages[currentImageIndex]}')`;
        }, 7000);
    }

    // 5. Rewards Page - Real Redeem Logic
    document.querySelectorAll('.redeem-form').forEach(form => {
        form.addEventListener('submit', (e) => {
            const confirmed = confirm('هل أنت متأكد من أنك تريد استبدال هذه المكافأة؟');
            if (!confirmed) {
                e.preventDefault();
            }
        });
    });

    // 6. Surveys Page - Load More Surveys (Dummy)
    const loadMoreBtn = document.getElementById('load-more-surveys');
    const surveyCardsGrid = document.querySelector('.survey-cards-grid');

    if (loadMoreBtn && surveyCardsGrid) {
        loadMoreBtn.addEventListener('click', () => {
            const dummySurveys = [
                {
                    title: "استبيان: التعليم عن بعد في سوريا",
                    points: "550 نقطة",
                    duration: "8 دقائق",
                    category: "تعليم"
                },
                {
                    title: "استبيان: تحديات الشباب في سوق العمل",
                    points: "650 نقطة",
                    duration: "12 دقيقة",
                    category: "مجتمع"
                },
                {
                    title: "استبيان: مستقبل الزراعة المستدامة",
                    points: "800 نقطة",
                    duration: "15 دقيقة",
                    category: "اقتصاد"
                }
            ];

            dummySurveys.forEach(survey => {
                const newCard = document.createElement('div');
                newCard.classList.add('survey-card-item');
                newCard.innerHTML = `
                    <h3>${survey.title}</h3>
                    <div class="survey-meta">
                        <span class="points">${survey.points}</span>
                        <span class="duration">${survey.duration}</span>
                        <span class="category">الفئة: ${survey.category}</span>
                    </div>
                    <p>شارك في هذا الاستبيان وساهم في فهم التحديات وتقديم الحلول.</p>
                    <a href="single-survey.html" class="button primary full-width">ابدأ الاستبيان</a>
                `;
                surveyCardsGrid.appendChild(newCard);
            });
        });
    }
});
