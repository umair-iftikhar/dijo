defmodule Dijo.Repo.Migrations.CreateLogs do
  use Ecto.Migration

  def change do
    create table(:logs) do
      add :log_type, :string
      add :log, :string
      add :project, :text

      timestamps()
    end
  end
end
