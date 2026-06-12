import { DataTable } from "../components/DataTable.jsx";
import { RecordForm } from "../components/RecordForm.jsx";
import { StatusBadge } from "../components/StatusBadge.jsx";
import { useAppData } from "../context/AppContext.jsx";
import { rectificationFields } from "../modules/forms.js";

const columns = [
  { key: "title", label: "Title" },
  { key: "project_name", label: "Project" },
  { key: "responsible", label: "Responsible" },
  { key: "priority", label: "Priority", render: (row) => <StatusBadge value={row.priority} /> },
  { key: "status", label: "Status", render: (row) => <StatusBadge value={row.status} /> },
  { key: "deadline", label: "Deadline" },
  { key: "created_at", label: "Created" },
  { key: "progress", label: "Progress notes" },
];

export function RectificationsPage() {
  const { rectifications, createRecord } = useAppData();

  const pendingCount = rectifications.filter((item) => item.status === "pending" || item.status === "in_progress").length;

  return (
    <div className="page-stack">
      <RecordForm
        title="Create rectification"
        fields={rectificationFields}
        onSubmit={(payload) => createRecord("rectifications", payload)}
      />
      <section className="panel">
        <div className="section-heading">
          <h2>Rectification Tasks</h2>
          <span>{pendingCount} pending</span>
        </div>
        <DataTable columns={columns} rows={rectifications} />
      </section>
    </div>
  );
}
