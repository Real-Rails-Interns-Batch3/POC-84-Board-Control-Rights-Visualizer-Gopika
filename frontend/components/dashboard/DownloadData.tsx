interface Props {
  data: unknown;
}

export default function DownloadData({
  data,
}: Props) {
  function downloadJSON() {
    const blob = new Blob(
      [JSON.stringify(data, null, 2)],
      {
        type: "application/json",
      }
    );

    const url =
      window.URL.createObjectURL(blob);

    const link =
      document.createElement("a");

    link.href = url;
    link.download = "board-control-data.json";

    link.click();
  }

  return (
    <button
      onClick={downloadJSON}
      className="w-full bg-cyan-600 hover:bg-cyan-700 rounded-lg p-3"
    >
      Download Sample Data
    </button>
  );
}