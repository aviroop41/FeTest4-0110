import React, { useEffect, useState } from 'react';

// Card component for displaying statistics
const StatsCard = ({ title, value, icon }) => (
  <div className="bg-white shadow-md rounded-lg p-4 m-2 text-center">
    <div className="text-lg font-semibold">{title}</div>
    <div className="text-2xl">{value}</div>
    <div>{icon}</div>
  </div>
);

// Main EmployeeDashboard component
const EmployeeDashboard = ({ employeeId }) => {
  const [attendance, setAttendance] = useState(null);
  const [leaveBalance, setLeaveBalance] = useState(null);
  const [recentActivities, setRecentActivities] = useState([]);
  const [error, setError] = useState(null);

  // Fetch attendance data
  const fetchAttendance = async () => {
    try {
      const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/attendance`);
      if (!response.ok) throw new Error('Failed to fetch attendance');
      const data = await response.json();
      setAttendance(data);
    } catch (err) {
      setError(err.message);
      setAttendance({ total: 0, present: 0 }); // Fallback data
    }
  };

  // Fetch leave balance data
  const fetchLeaveBalance = async () => {
    try {
      const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/leave-balance`);
      if (!response.ok) throw new Error('Failed to fetch leave balance');
      const data = await response.json();
      setLeaveBalance(data);
    } catch (err) {
      setError(err.message);
      setLeaveBalance({ total: 0, used: 0 }); // Fallback data
    }
  };

  // Fetch recent activities data
  const fetchRecentActivities = async () => {
    try {
      const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/recent-activities`);
      if (!response.ok) throw new Error('Failed to fetch recent activities');
      const data = await response.json();
      setRecentActivities(data);
    } catch (err) {
      setError(err.message);
      setRecentActivities([]); // Fallback data
    }
  };

  useEffect(() => {
    fetchAttendance();
    fetchLeaveBalance();
    fetchRecentActivities();
  }, [employeeId]);

  return (
    <div className="p-4">
      {error && <div className="text-red-600">{error}</div>}
      <div className="grid grid-cols-3 gap-4">
        <StatsCard title="Attendance" value={`${attendance?.present}/${attendance?.total}`} icon={<i className="fas fa-user-check"></i>} />
        <StatsCard title="Leave Balance" value={`${leaveBalance?.total - leaveBalance?.used}`} icon={<i className="fas fa-plane"></i>} />
        <div className="bg-white shadow-md rounded-lg p-4 m-2">
          <h3 className="font-semibold">Recent Activities</h3>
          <ul>
            {recentActivities.map((activity, index) => (
              <li key={index} className="border-b py-2">
                {activity.description}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default EmployeeDashboard;