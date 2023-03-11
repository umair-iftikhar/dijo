defmodule DijoWeb.LogLive.Show do
  use DijoWeb, :live_view

  alias Dijo.Logs

  @impl true
  def mount(_params, _session, socket) do
    {:ok, socket}
  end

  @impl true
  def handle_params(%{"id" => id}, _, socket) do
    {:noreply,
     socket
     |> assign(:page_title, page_title(socket.assigns.live_action))
     |> assign(:log, Logs.get_log!(id))}
  end

  defp page_title(:show), do: "Show Log"
  defp page_title(:edit), do: "Edit Log"
end
