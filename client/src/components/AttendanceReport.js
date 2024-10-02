import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2'; // Chart.js for visualizations
import { Chart, registerables } from 'chart.js'; // Import Chart.js
Chart.register(...registerables); // Register necessary components

const AttendanceReport = ({ managerId }) => {
    const [attendanceData, setAttendanceData] = useState([]);
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [error, setError] = useState('');

    const fetchAttendanceData = async () => {
        try {
            const response = await fetch(`/api/manager/${managerId}/attendance-reports?start_date=${startDate}&end_date=${endDate}`);
            if (!response.ok) throw new Error('Failed to fetch data');
            const data = await response.json();
            setAttendanceData(data);
        } catch (err) {
            setError('Could not load attendance data, showing mock data.');
            // Mock data for demonstration purposes
            setAttendanceData([
                { date: '2023-01-01', attendance: 30 },
                { date: '2023-01-02', attendance: 25 },
                { date: '2023-01-03', attendance: 28 },
                { date: '2023-01-04', attendance: 32 },
            ]);
        }
    };

    useEffect(() => {
        if (startDate && endDate) {
            fetchAttendanceData();
        }
    }, [startDate, endDate]);

    const handleDateChange = () => {
        if (startDate && endDate) {
            fetchAttendanceData();
        }
    };

    const chartData = {
        labels: attendanceData.map(item => item.date),
        datasets: [
            {
                label: 'Attendance',
                data: attendanceData.map(item => item.attendance),
                borderColor: 'rgba(0, 123, 255, 1)', // Ensure color is in rgba format
                backgroundColor: 'rgba(0, 123, 255, 0.3)',
                fill: true, // Enable filling under the line
            },
        ],
    };

    return (
        <div className="p-6 bg-white rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-4">Attendance Report</h2>
            <div className="flex space-x-4 mb-4">
                <input
                    type="date"
                    className="border rounded pyl-2 px-3"
                    value={startDate}
                    onChange={(e) => setStartDate(e.target.value)}
                    aria-label="Start Date"
                />
                <input
                    type="date"
                    className="border rounded pyl-2 px-3"
                    value={endDate}
                    onChange={(e) => setEndDate(e.target.value)}
                    aria-label="End Date"
                />
                <button 
                    className="bg-blue-500 text-white px-4 py-2 rounded" 
                    onClick={handleDateChange} 
                    aria-label="Generate Report"
                >
                    Generate Report
                </button>
            </div>
            <Line data={chartData} />
        </div>
    );
};

export default AttendanceReport;