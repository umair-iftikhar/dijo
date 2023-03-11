defmodule Dijo.Logs.Log do
  use Ecto.Schema
  import Ecto.Changeset

  schema "logs" do
    field :log, :string
    field :log_type, :string
    field :project, :string

    timestamps()
  end

  @doc false
  def changeset(log, attrs) do
    log
    |> cast(attrs, [:log_type, :log, :project])
    |> validate_required([:log_type, :log, :project])
  end
end
