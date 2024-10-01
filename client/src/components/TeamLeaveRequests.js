import React, { useEffect, useState } from 'react';

const TeamLeaveRequests = ({ managerId }) => {
  const [leaveRequests, setLeaveRequests] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8080/api/manager/${managerId}/team-leave-requests`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => setLeaveRequests(data))
      .catch(error => {
        console.error('Error fetching leave requests:', error);
        setError('Failed to load leave requests. Showing mock data.');
        // Fallback to mock data
        setLeaveRequests([
          { id: 1, name: 'John Doe', date: '2023-11-01', status: 'Pending' },
          { id: 2, name: 'Jane Smith', date: '2023-11-15', status: 'Pending' },
          { id: 3, name: 'Bob Johnson', date: '2023-11-20', status: 'Pending' },
        ]);
      });
  }, [managerId]);

  const handleApproval = (requestId) => {
    fetch(`http://localhost:8080/api/manager/${managerId}/leave-requests/${requestId}/approve`, { method: 'POST' })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        // Update state to reflect approved request
        setLeaveRequests(prev => prev.filter(request => request.id !== requestId));
      })
      .catch(error => {
        console.error('Error approving leave request:', error);
        alert('Failed to approve the leave request.');
      });
  };

  const handleDenial = (requestId) => {
    fetch(`http://localhost:8080/api/manager/${managerId}/leave-requests/${requestId}/deny`, { method: 'POST' })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        // Update state to reflect denied request
        setLeaveRequests(prev => prev.filter(request => request.id !== requestId));
      })
      .catch(error => {
        console.error('Error denying leave request:', error);
        alert('Failed to deny the leave request.');
      });
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Pending Leave Requests</h2>
      {error && <p className="text-red-600">{error}</p>}
      <ul className="space-y-4">
        {leaveRequests.map(request => (
          <li key={request.id} className="p-4 border rounded-lg shadow-md flex justify-between items-center">
            <div>
              <p className="font-semibold">{request.name}</p>
              <p>Date Requested: {request.date}</p>
              <p>Status: {request.status}</p>
            </div>
            <div className="flex space-x-2">
              <button
                onClick={() => handleApproval(request.id)}
                className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-400"
                aria-label={`Approve leave request from ${request.name}`}
              >
                Approve
              </button>
              <button
                onClick={() => handleDenial(request.id)}
                className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-400"
                aria-label={`Deny leave request from ${request.name}`}
              >
                Deny
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TeamLeaveRequests;