document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------------------
    // 1. Smooth Scrolling for Navigation Links
    // ----------------------------------------------------
    document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            if (targetId && targetId !== '#') {
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // ----------------------------------------------------
    // 2. Auth Page - Login/Signup Tab Switching & Validation
    // ----------------------------------------------------
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

        // Initial state: Login form active by default when page loads
        switchAuthTab(loginTab, signupTab, loginForm, signupForm);

        loginTab.addEventListener('click', () => {
            switchAuthTab(loginTab, signupTab, loginForm, signupForm);
        });

        signupTab.addEventListener('click', () => {
            switchAuthTab(signupTab, loginTab, signupForm, loginForm);
        });

        // --- Login Form Validation ---
        loginForm.addEventListener('submit', (e) => {
            // Check HTML5 validation first
            if (!loginForm.checkValidity()) {
                e.preventDefault(); // Stop form submission if invalid
                return; // Exit if browser validation fails
            }

            // Additional custom validation can go here if needed (e.g., specific email domain checks)
            // For now, HTML5 validation is sufficient for basic checks.

            // If all checks pass, you'd send data to backend. For now, a placeholder alert.
            // e.preventDefault(); // Uncomment if you don't want the form to actually submit (e.g., to a dummy URL)
            alert('تم محاولة تسجيل الدخول بنجاح! (هذا مثال فقط)');
            // In a real app: submit login credentials via AJAX
        });

        // --- Signup Form Validation ---
        signupForm.addEventListener('submit', (e) => {
            // Check HTML5 validation first (for 'required', 'email' type, etc.)
            if (!signupForm.checkValidity()) {
                e.preventDefault(); // Stop form submission if invalid
                return; // Exit if browser validation fails
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
                e.preventDefault(); // Prevent form submission
                alert('كلمتا المرور غير متطابقتين. يرجى التأكد.');
                document.getElementById('signup-confirm-password').focus();
                return;
            }

            // If all checks pass, you'd send data to backend. For now, a placeholder alert.
            // e.preventDefault(); // Uncomment if you don't want the form to actually submit
            alert('تم محاولة إنشاء حساب بنجاح! (هذا مثال فقط)');
            // In a real app: submit signup data via AJAX
        });
    }

    // ----------------------------------------------------
    // 3. Single Survey Page - "Other" option for questions & Progress Bar & Success Modal
    // ----------------------------------------------------
    const surveyForm = document.getElementById('surveyForm');
    const questions = document.querySelectorAll('.form-question');
    const prevBtn = document.getElementById('prev-question-btn');
    const nextBtn = document.getElementById('next-question-btn');
    const submitBtn = document.getElementById('submit-survey-btn');
    const progressBar = document.getElementById('survey-progress-bar');
    const progressText = document.getElementById('progress-text');

    // Modal elements
    const successModal = document.getElementById('successModal');
    const closeButton = successModal ? successModal.querySelector('.close-button') : null;
    const modalPointsSpan = successModal ? successModal.querySelector('.modal-content p span') : null;

    let currentQuestionIndex = 0;
    const totalQuestions = questions.length;
    const surveyPoints = 700; // Points awarded for this survey

    if (surveyForm && questions.length > 0) {

        // Function to update progress bar
        const updateProgressBar = () => {
            const progress = ((currentQuestionIndex + 1) / totalQuestions) * 100;
            progressBar.style.width = `${progress}%`;
            progressText.textContent = `${Math.round(progress)}% مكتمل`;
        };

        // Function to show current question and hide others
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

            // Handle button visibility
            prevBtn.style.display = (index === 0) ? 'none' : 'inline-block';
            nextBtn.style.display = (index === totalQuestions - 1) ? 'none' : 'inline-block';
            submitBtn.style.display = (index === totalQuestions - 1) ? 'inline-block' : 'none';

            updateProgressBar();
        };

        // Initial display
        showQuestion(currentQuestionIndex);

        // Event listener for "Next" button
        nextBtn.addEventListener('click', () => {
            // Basic validation for the current question before moving to the next
            // Checks for required inputs within the current question's div
            const currentQuestionInputs = questions[currentQuestionIndex].querySelectorAll('input[required], textarea[required]');
            let isValid = true;
            currentQuestionInputs.forEach(input => {
                if (!input.checkValidity()) {
                    isValid = false;
                    // Trigger browser's native validation message
                    input.reportValidity();
                }
            });

            if (isValid && currentQuestionIndex < totalQuestions - 1) {
                currentQuestionIndex++;
                showQuestion(currentQuestionIndex);
            }
        });

        // Event listener for "Previous" button
        prevBtn.addEventListener('click', () => {
            if (currentQuestionIndex > 0) {
                currentQuestionIndex--;
                showQuestion(currentQuestionIndex);
            }
        });

        // Event listener for form submission (for the last question)
        surveyForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // In a real application, you would collect all answers and send them to a backend server here.
            // For now, we'll just show the success modal.

            if (successModal) {
                if (modalPointsSpan) {
                    modalPointsSpan.textContent = surveyPoints; // Update points in modal
                }
                successModal.classList.remove('hidden');
                successModal.classList.add('visible'); // Add visible class for flex display
            }
        });

        // Event listener for closing the modal using the close button
        if (closeButton) {
            closeButton.addEventListener('click', () => {
                successModal.classList.add('hidden');
                successModal.classList.remove('visible');
            });
        }
        // Event listener for closing the modal if clicking outside the modal content
        if (successModal) {
            successModal.addEventListener('click', (e) => {
                // Check if the click occurred directly on the overlay, not its children
                if (e.target === successModal) {
                    successModal.classList.add('hidden');
                    successModal.classList.remove('visible');
                }
            });
        }

        // "Other" option for the first question (q1) logic
        const q1Radios = document.querySelectorAll('input[name="q1"]');
        const q1OtherTextarea = document.querySelector('textarea[name="q1_other"]');

        if (q1Radios.length > 0 && q1OtherTextarea) {
            q1Radios.forEach(radio => {
                radio.addEventListener('change', () => {
                    if (radio.value === 'مصادر أخرى') {
                        q1OtherTextarea.classList.remove('hidden');
                        q1OtherTextarea.setAttribute('required', 'true'); // Make "other" field required
                    } else {
                        q1OtherTextarea.classList.add('hidden');
                        q1OtherTextarea.removeAttribute('required'); // Remove required attribute
                    }
                });
            });
            // Initial check for q1 "Other" on page load
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


    // ----------------------------------------------------
    // 4. Hero Section - Dynamic Background Image (Example)
    // You can replace these with actual image URLs.
    // ----------------------------------------------------
    const heroSection = document.querySelector('.hero');
    const backgroundImages = [
        'https://images.unsplash.com/photo-1596568165034-7a134a6d714b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', // Example Syrian landscape 1
        'https://images.unsplash.com/photo-1551608460-6dd831c2bbd3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', // Example Syrian landscape 2
        'https://images.unsplash.com/photo-1579730538749-d3e2300b9795?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'  // Example Syrian landscape 3
    ];
    let currentImageIndex = 0;

    if (heroSection && backgroundImages.length > 0) {
        // Set initial background image
        heroSection.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('${backgroundImages[currentImageIndex]}')`;

        // Change background image every 7 seconds
        setInterval(() => {
            currentImageIndex = (currentImageIndex + 1) % backgroundImages.length;
            heroSection.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('${backgroundImages[currentImageIndex]}')`;
        }, 7000); // Change every 7 seconds (7000 milliseconds)
    }

    // ----------------------------------------------------
    // 5. Rewards Page - Redeem Reward Functionality (Dummy)
    // ----------------------------------------------------
    const currentPointsSpan = document.getElementById('current-points');
    if (currentPointsSpan) {
        let userPoints = 1500; // Default user points
        currentPointsSpan.textContent = userPoints;

        document.querySelectorAll('.redeem-button').forEach(button => {
            button.addEventListener('click', (e) => {
                e.preventDefault(); // Prevent default button behavior (e.g., form submission)

                const card = e.target.closest('.reward-card');
                const pointsCostText = card.querySelector('.points-cost').textContent;
                // Extract only the number from the text (e.g., "700 نقطة" -> 700)
                const pointsCost = parseInt(pointsCostText.replace(' نقطة', '').replace(' نقطة', ''));

                if (userPoints >= pointsCost) {
                    userPoints -= pointsCost;
                    currentPointsSpan.textContent = userPoints;
                    alert(`تم استبدال المكافأة بنجاح! تبقى لديك ${userPoints} نقطة.`);
                    // In a real application, you would add logic here to confirm phone number or send a real request
                } else {
                    alert('نقاطك غير كافية لاستبدال هذه المكافأة.');
                }
            });
        });
    }

    // ----------------------------------------------------
    // 6. Surveys Page - Load More Surveys (Dummy)
    // ----------------------------------------------------
    const loadMoreBtn = document.getElementById('load-more-surveys');
    const surveyCardsGrid = document.querySelector('.survey-cards-grid');

    if (loadMoreBtn && surveyCardsGrid) {
        loadMoreBtn.addEventListener('click', () => {
            // Simulate loading new surveys
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

            alert('تم تحميل المزيد من الاستبيانات!');
            // You could hide or disable the button after loading if there are no more surveys
            // loadMoreBtn.style.display = 'none';
        });
    }
});