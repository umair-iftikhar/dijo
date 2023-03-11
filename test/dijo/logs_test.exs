defmodule Dijo.LogsTest do
  use Dijo.DataCase

  alias Dijo.Logs

  describe "logs" do
    alias Dijo.Logs.Log

    import Dijo.LogsFixtures

    @invalid_attrs %{log: nil, log_type: nil, project: nil}

    test "list_logs/0 returns all logs" do
      log = log_fixture()
      assert Logs.list_logs() == [log]
    end

    test "get_log!/1 returns the log with given id" do
      log = log_fixture()
      assert Logs.get_log!(log.id) == log
    end

    test "create_log/1 with valid data creates a log" do
      valid_attrs = %{log: "some log", log_type: "some log_type", project: "some project"}

      assert {:ok, %Log{} = log} = Logs.create_log(valid_attrs)
      assert log.log == "some log"
      assert log.log_type == "some log_type"
      assert log.project == "some project"
    end

    test "create_log/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = Logs.create_log(@invalid_attrs)
    end

    test "update_log/2 with valid data updates the log" do
      log = log_fixture()
      update_attrs = %{log: "some updated log", log_type: "some updated log_type", project: "some updated project"}

      assert {:ok, %Log{} = log} = Logs.update_log(log, update_attrs)
      assert log.log == "some updated log"
      assert log.log_type == "some updated log_type"
      assert log.project == "some updated project"
    end

    test "update_log/2 with invalid data returns error changeset" do
      log = log_fixture()
      assert {:error, %Ecto.Changeset{}} = Logs.update_log(log, @invalid_attrs)
      assert log == Logs.get_log!(log.id)
    end

    test "delete_log/1 deletes the log" do
      log = log_fixture()
      assert {:ok, %Log{}} = Logs.delete_log(log)
      assert_raise Ecto.NoResultsError, fn -> Logs.get_log!(log.id) end
    end

    test "change_log/1 returns a log changeset" do
      log = log_fixture()
      assert %Ecto.Changeset{} = Logs.change_log(log)
    end
  end
end
