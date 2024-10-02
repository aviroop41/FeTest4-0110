import React, { useState } from 'react';

// LeaveRequestForm component for submitting leave requests
const LeaveRequestForm = () => {
    // Local state for the form inputs
    const [leaveType, setLeaveType] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [reason, setReason] = useState('');
    const [error, setError] = useState('');
    const [successMessage, setSuccessMessage] = useState('');

    // Mock function to simulate an API call
    const mockApiCall = () => {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if (leaveType && startDate && endDate && reason) {
                    resolve({ status: 'success' });
                } else {
                    reject({ status: 'error', message: 'All fields are required' });
                }
            }, 500);
        });
    };

    // Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setSuccessMessage('');

        try {
            const response = await mockApiCall();
            setSuccessMessage('Leave request submitted successfully!');
            // Reset form fields
            setLeaveType('');
            setStartDate('');
            setEndDate('');
            setReason('');
        } catch {
            // Mock data in case of submit failure
            setSuccessMessage('Leave request submission failed. Mock data used.');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="p-4 bg-white shadow-md rounded-lg">
            <h2 className="text-lg font-semibold mb-4">Leave Request Form</h2>
            {error && <div className="mb-4 text-red-500">{error}</div>}
            {successMessage && <div className="mb-4 text-green-500">{successMessage}</div>}

            <label htmlFor="leaveType" className="block text-sm font-medium text-gray-700">Leave Type</label>
            <select
                id="leaveType"
                value={leaveType}
                onChange={(e) => setLeaveType(e.target.value)}
                className="mt-1 block w-full p-2 border rounded-md"
                required
            >
                <option value="">Select leave type</option>
                <option value="sick">Sick Leave</option>
                <option value="vacation">Vacation Leave</option>
                <option value="personal">Personal Leave</option>
            </select>

            <label htmlFor="startDate" className="block text-sm font-medium text-gray-700 mt-4">Start Date</label>
            <input
                type="date"
                id="startDate"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
                className="mt-1 block w-full p-2 border rounded-md"
                required
            />

            <label htmlFor="endDate" className="block text-sm font-medium text-gray-700 mt-4">End Date</label>
            <input
                type="date"
                id="endDate"
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
                className="mt-1 block w-full p-2 border rounded-md"
                required
            />

            <label htmlFor="reason" className="block text-sm font-medium text-gray-700 mt-4">Reason</label>
            <textarea
                id="reason"
                value={reason}
                onChange={(e) => setReason(e.target.value)}
                className="mt-1 block w-full p-2 border rounded-md"
                rows={4}
                required
            />

            <button
                type="submit"
                className="mt-6 w-full bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600"
            >
                Submit Request
            </button>
        </form>
    );
};

export default LeaveRequestForm;