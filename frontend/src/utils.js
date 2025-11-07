// Production backend URL - replace with your actual Render URL after deployment
export const SERVER_URL = process.env.NODE_ENV === 'production' 
  ? "https://fingrow-ai-backend.onrender.com" 
  : "http://127.0.0.1:5000";

// Function to calculate income tax based on Indian tax slabs
export const calculateIncomeTax = (annualIncome) => {
  // For Financial Year 2023-24 (Assessment Year 2024-25)
  // New tax regime (default)
  let tax = 0;
  
  if (annualIncome <= 300000) {
    tax = 0;
  } else if (annualIncome <= 600000) {
    tax = (annualIncome - 300000) * 0.05;
  } else if (annualIncome <= 900000) {
    tax = 15000 + (annualIncome - 600000) * 0.10;
  } else if (annualIncome <= 1200000) {
    tax = 45000 + (annualIncome - 900000) * 0.15;
  } else if (annualIncome <= 1500000) {
    tax = 90000 + (annualIncome - 1200000) * 0.20;
  } else {
    tax = 150000 + (annualIncome - 1500000) * 0.30;
  }
  
  // Adding 4% health and education cess
  const cess = tax * 0.04;
  return tax + cess;
};

// Function to format currency in Indian format
export const formatIndianCurrency = (amount) => {
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0
  }).format(amount);
};