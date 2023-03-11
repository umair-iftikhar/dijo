defmodule DijoWeb.Router do
  use DijoWeb, :router

  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_live_flash
    plug :put_root_layout, {DijoWeb.Layouts, :root}
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/", DijoWeb do
    pipe_through :browser

    live "/logs", LogLive.Index, :index
    live "/logs/new", LogLive.Index, :new
    live "/logs/:id/edit", LogLive.Index, :edit

    live "/logs/:id", LogLive.Show, :show
    live "/logs/:id/show/edit", LogLive.Show, :edit

    get "/", PageController, :home
  end

  # Other scopes may use custom stacks.
  # scope "/api", DijoWeb do
  #   pipe_through :api
  # end

  # Enable LiveDashboard and Swoosh mailbox preview in development
  if Application.compile_env(:dijo, :dev_routes) do
    # If you want to use the LiveDashboard in production, you should put
    # it behind authentication and allow only admins to access it.
    # If your application does not have an admins-only section yet,
    # you can use Plug.BasicAuth to set up some basic authentication
    # as long as you are also using SSL (which you should anyway).
    import Phoenix.LiveDashboard.Router

    scope "/dev" do
      pipe_through :browser

      live_dashboard "/dashboard", metrics: DijoWeb.Telemetry
      forward "/mailbox", Plug.Swoosh.MailboxPreview
    end
  end
end
