defmodule Dijo.LogsFixtures do
  @moduledoc """
  This module defines test helpers for creating
  entities via the `Dijo.Logs` context.
  """

  @doc """
  Generate a log.
  """
  def log_fixture(attrs \\ %{}) do
    {:ok, log} =
      attrs
      |> Enum.into(%{
        log: "some log",
        log_type: "some log_type",
        project: "some project"
      })
      |> Dijo.Logs.create_log()

    log
  end
end
